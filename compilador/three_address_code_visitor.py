import re
from grammar.yaplListener import yaplListener
from grammar.yaplParser import yaplParser
from grammar.yaplVisitor import yaplVisitor
from symbol_table import SymbolTable

class TAC_VISITOR(yaplVisitor):
    def __init__(self, tac_listener):
        self.tac = {}  
        self.temporals = 0  
        self.param_count = 0
        self.labels = 0  
        self.class_name = None
        self.method_name = None
        
        self.aux_code = []
        self.memory_allocation = {}
        self.memory = 0
        self.is_accessed = False
        self.listener = tac_listener
        self.temporal_list = {}
        self.arguments = {}
        self.type_operation= ""
        self.params = []

    def append_aux_code(self, code): #Agrega código a una lista de código auxiliar.
        if self.method_name:
            if code[0] == self.method_name + ':': 
                self.aux_code.append(code)
            else:
                line = ('  ',) + code
                self.aux_code.append(line)
        else:
            self.aux_code.append(code)

    def set_memory(self): #Gestión de la asignación y actualización de la memoria para clases y métodos.
        self.memory = 0

    def update_memory(self, size): #Gestión de la asignación y actualización de la memoria para clases y métodos.
        self.memory += size
        key = f"{self.class_name}.{self.method_name}" if self.method_name else self.class_name 
        if self.method_name:
            self.memory_allocation[key] += self.memory
            self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"][0] = f"Begin Class {self.memory_allocation[key]}"
        else:
            self.memory_allocation[key] += self.memory
            self.tac[self.class_name][0] = f"Begin Class {self.memory_allocation[key]}"
        self.set_memory()

    def set_memory_for_class(self): #Gestión de la asignación y actualización de la memoria para clases y métodos.
        self.memory_allocation[self.class_name] = self.memory
        self.set_memory()

    def set_memory_for_method(self): #Gestión de la asignación y actualización de la memoria para clases y métodos.
        key = f"{self.class_name}.{self.method_name}"
        self.memory_allocation[key] = self.memory
        self.set_memory()

    def generate_temporal(self): # Genera nombres de variables temporales.
        temporal = f"$t{self.temporals}"  # Genera un nombre de variable temporal con el contador actual
        self.temporals += 1  # Incrementa el contador de variables temporales
        return temporal  # Retorna el nombre de la variable temporal generada

    def generate_argument(self): # Genera nombres de argumentos.
        argument = f"$a{self.param_count}"  # Genera un nombre de argumento con el contador actual
        self.param_count += 1  # Incrementa el contador de argumentos
        return argument  # Retorna el nombre del argumento generado

    def is_temporal_created(self, variable): 
        if variable in self.temporal_list:  # Verifica si el nombre de la variable está en el diccionario de variables temporales
            return self.temporal_list[variable]  # Retorna el content asociado al nombre de la variable temporal
        return None  # Retorna None si el nombre de la variable no se encuentra en el diccionario de variables temporales

    def is_argument_created(self, variable): # Verifica si el $a existe
        if variable in self.arguments:
            return self.arguments[variable]
        return None

    def generate_label(self): #Genera nombres de etiquetas.
        self.labels += 1
        return f"label{self.labels}"

    
    
    def visitClassDeclaration(self, ctx: yaplParser.ClassDeclarationContext):
        self.class_name = ctx.TYPE_ID()[0].getText()
        self.method_name = ""
        self.tac[self.class_name] = []
        self.tac[self.class_name].append("Begin Class")
        self.set_memory_for_class()
        self.visitChildren(ctx)
        self.tac[self.class_name].append("End Class")


    def visitAttributeDeclaration(self, ctx: yaplParser.AttributeDeclarationContext):
        variable = ctx.ID().getText()
        if ctx.ID():
            expression_result = ctx.type_().getText()
            self.tac[self.class_name].append( f"{variable} = {expression_result}")

            
            self.append_aux_code(('ASSIGN', expression_result, '-', variable))
        size = self.get_size(ctx.type_().getText())
        self.update_memory(size)

    def visitAssignmentDeclaration(self, ctx: yaplParser.AssignmentDeclarationContext):
        variable = ctx.ID().getText()
        expression_result = ctx.expression().getText()
        children = self.visit(ctx.expression())

        if children: # equals to children
            self.tac[self.class_name].append(f"{variable} = {children}")
            self.append_aux_code(('ASSIGN', children, '-', variable))
        else:
            self.tac[self.class_name].append(f"{variable} = {expression_result}")
            self.append_aux_code(('<-', expression_result, '-', variable))

    def visitMethodDeclaration(self, ctx: yaplParser.MethodDeclarationContext):
        
        self.method_name = ""
        self.method_name = ctx.ID().getText()
        self.tac[self.class_name].append({f"{self.class_name}.{self.method_name}:": []})
        self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"].append(
            "Begin Function")
        self.append_aux_code((f"{self.method_name}:",))
        self.set_memory_for_method()
        self.visitChildren(ctx)
        if self.method_name != "main":
            self.append_aux_code(('jr', "$ra"))
        else:
            self.append_aux_code(('li', '$v0', '10'))
            self.append_aux_code(("syscall", ""))
        self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"].append("End Function")
        self.method_name = ""

    def visitParameterList(self, ctx: yaplParser.ParameterListContext): #PARAMETROS
        self.visitChildren(ctx)


    def visitParameter(self, ctx: yaplParser.ParameterContext): #PARAMETROS
        self.params.append(ctx.ID().getText())
        size = self.get_size(ctx.type_().getText())
        self.update_memory(size)

    def visitMethodCallStatement(self, ctx: yaplParser.MethodCallStatementContext): #LLAMADA A METODO
        # Obtiene el nombre del método llamado
        method_name = ctx.ID().getText()
        
        # Obtiene una referencia al código intermedio asociado al método actual en la clase actual
        tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        
        # Verifica si hay argumentos en la llamada al método
        if ctx.expressionList():
            # Recorre cada argumento de la llamada al método
            for expression in ctx.expressionList().expression():
                # Genera nombres temporales y de argumentos si no existen
                temporal = self.is_temporal_created(expression.getText()) or self.generate_temporal()
                argument = self.is_argument_created(expression.getText()) or self.generate_argument()
                
                # Asocia el argumento con su representación en el código intermedio
                self.arguments[expression.getText()] = argument
                
                # Agrega una instrucción al código intermedio para empujar el valor del argumento a la pila
                tac.append(f"PUSH PARAM {temporal}")
                
                # Agrega código intermedio para mover el valor del argumento a su lugar correspondiente para la llamada al método
                self.append_aux_code(('move', argument, temporal))
            
            # Verifica si el método es 'out_int' para imprimir un entero
            if method_name == 'out_int':
                self.append_aux_code(('lw', '$a0', expression.getText()))
                self.append_aux_code(('li', '$v0', '1'))
                self.append_aux_code(('syscall',))
            else:
                # Agrega código intermedio para realizar la llamada al método
                self.append_aux_code(('jal', method_name))
        
        # Verifica si se estaba accediendo a algo
        if self.is_accessed:
            # Restablece la bandera y devuelve un mensaje indicando la llamada al método
            self.is_accessed = False
            return f"Call {method_name}()"
        else:
            # Agrega una instrucción al código intermedio para realizar la llamada al método
            tac.append(f"Call {method_name}()")


    def visitLetDeclaration(self, ctx: yaplParser.LetDeclarationContext): #DECLARACION DE VARIABLES
        for id, type in enumerate(ctx.type_()):
            self.tac[self.class_name].append(f"{ctx.ID()[id].getText()} = {type.getText()}")
            size = self.get_size(type.getText())
            self.update_memory(size)
        self.visitChildren(ctx)

    def visitAdditionExpression(self, ctx: yaplParser.AdditionExpressionContext): #SUMA
        left = self.visit(ctx.expression(0)) or ctx.expression(0).getText()
        right = self.visit(ctx.expression(1)) or ctx.expression(1).getText()
        temporal = self.generate_temporal()
        self.append_aux_code(('+', left, right, temporal))
        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]
        tac.append(f"{temporal} = {left} + {right}")
        return temporal

    def visitSubtractionExpression(self, ctx: yaplParser.SubtractionExpressionContext): #RESTA
        left = self.visit(ctx.expression(0)) or ctx.expression(0).getText()
        right = self.visit(ctx.expression(1)) or ctx.expression(1).getText()
        temporal = self.generate_temporal()

        self.append_aux_code(('-', left, right, temporal))

        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]

        tac.append(f"{temporal} = {left} - {right}")
        return temporal

    def visitMultiplicationExpression(self, ctx: yaplParser.MultiplicationExpressionContext): #MULTIPLICACION
            left = self.visit(ctx.expression(0)) or ctx.expression(0).getText()
            right = self.visit(ctx.expression(1)) or ctx.expression(1).getText()
            temporal = self.generate_temporal()

            self.append_aux_code(('mul', temporal, left, right))

            if self.method_name:
                tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
            else:
                tac = self.tac[self.class_name]

            tac.append(f"{temporal} = {left} * {right}")
            return temporal


    def visitDivisionExpression(self, ctx: yaplParser.DivisionExpressionContext): #DIVISION
        left = self.visit(ctx.expression(0)) or ctx.expression(0).getText()
        right = self.visit(ctx.expression(1)) or ctx.expression(1).getText()
        temporal = self.generate_temporal()

        self.cuadruplos.append(('/', left, right, temporal))
        self.append_aux_code(('/', left, right, temporal))

        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]

        tac.append(f"{temporal} = {left} / {right}")
        return temporal

    def visitNewExpression(self, ctx: yaplParser.NewExpressionContext): 
        pass
    
    def visitIfStatement(self, ctx: yaplParser.IfStatementContext): #IF
        end = self.generate_label()
        else_label = self.generate_label()
        temporal = self.visit(ctx.expression()) or ctx.expression().getText()

        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]

        tac.append(f"if false {temporal} goto {else_label}")
        self.append_aux_code(('<-', ctx.expression().getText(), '-', temporal))
        self.append_aux_code(('if false', temporal, '-', else_label))
        self.visit(ctx.statement(0))
        tac.append(f"goto {end}")
        tac.append(f"{else_label}:")
        if ctx.statement(1):
            self.visit(ctx.statement(1))
        tac.append(f"{end}")

    def visitExpressionStatement(self, ctx: yaplParser.ExpressionStatementContext):
        self.visit(ctx.expression())

    def visitGreaterThanExpression(self, ctx: yaplParser.GreaterThanExpressionContext): #MAYOR QUE
        left = self.visit(ctx.expression(0)) or ctx.expression(0).getText()
        right = self.visit(ctx.expression(1)) or ctx.expression(1).getText()
        temporal = self.generate_temporal()

        self.append_aux_code(('>', left, right, '-'))

        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]

        tac.append(f"{temporal} = {left} > {right}")
        return temporal

    def visitLessThanExpression(self, ctx: yaplParser.LessThanExpressionContext): #MENOR QUE
        left = self.visit(ctx.expression(0)) or ctx.expression(0).getText()
        right = self.visit(ctx.expression(1)) or ctx.expression(1).getText()
        temporal = self.generate_temporal()

        self.append_aux_code(('<', left, right, '-'))

        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]

        tac.append(f"{temporal} = {left} < {right}")
        return temporal

    def visitEqualityExpression(self, ctx: yaplParser.EqualityExpressionContext): #IGUAL
        left = self.visit(ctx.expression(0)) or ctx.expression(0).getText()
        right = self.visit(ctx.expression(1)) or ctx.expression(1).getText()
        temporal = self.generate_temporal()

        self.append_aux_code(('==', left, right, '-'))

        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]

        tac.append(f"{temporal} = {left} == {right}")
        return temporal

    def visitNotEqualExpression(self, ctx: yaplParser.NotEqualExpressionContext): #DIFERENTE
        left = self.visit(ctx.expression(0)) or ctx.expression(0).getText()
        right = self.visit(ctx.expression(1)) or ctx.expression(1).getText()
        temporal = self.generate_temporal()

        self.append_aux_code(('!=', left, right, '-'))

        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]

        tac.append(f"{temporal} = {left} != {right}")
        return temporal


    def visitAssignmentExpression(self, ctx: yaplParser.AssignmentExpressionContext): #ASIGNACION
        left = self.visit(ctx.expression(0)) or ctx.expression(0).getText()
        right = self.visit(ctx.expression(1)) or ctx.expression(1).getText()

        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]

        tac.append(f"{left} = {right}")

        for context in self.listener.symbol_table.context:
            if left in context:
                if 'accessed' in context[left] and context[left]['accessed']:
                    break
                else:
                    temporal = self.is_temporal_created(left) or self.generate_temporal()
                    self.temporal_list[left] = temporal
                    self.append_aux_code(('li', temporal, left))
                    self.append_aux_code(('sw', temporal, right))

    def visitVariableDeclaration(self, ctx: yaplParser.VariableDeclarationContext): #DECLARACION DE VARIABLES
        variable = ctx.ID().getText()
        expression_result = ctx.type_().getText()

        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]

        if ctx.statement():
            tac.append(f"{variable} = {expression_result}")
            self.append_aux_code(('ASSIGN1', expression_result, '-', variable))
            if re.search(r'[\+\-\*\/]', ctx.statement().getText()) or re.search(r'[(]', ctx.statement().getText()):
                self.is_accessed = True
                right_side = self.visit(ctx.statement())
            else:
                right_side = ctx.statement().getText()
            tac.append(f"{variable} = {right_side}")
            self.append_aux_code(('<-', variable, '-', right_side))
        else:
            tac.append(f"{variable} = {expression_result}")

            for context in self.listener.symbol_table.context:
                if variable in context:
                    if 'accessed' in context[variable] and context[variable]['accessed']:
                        break
                    else:
                        temporal = self.is_temporal_created(variable) or self.generate_temporal()
                        self.temporal_list[variable] = temporal
                        self.append_aux_code(('lw', temporal, variable))
        size = self.get_size(ctx.type_().getText())
        self.update_memory(size)

    def visitReturnStatement(self, ctx: yaplParser.ReturnStatementContext): #RETURN
        if self.method_name:
            if ctx.expression():
                expression = ctx.expression().getText()
                self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"].append(f"return {expression}")
                self.append_aux_code(('return', '-', '-',  expression))
            else:
                self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"].append(f"return")
                self.append_aux_code(('return', '-', '-', '-'))
        else:
            if ctx.expression():
                expression = ctx.expression().getText()
                self.tac[self.class_name].append(f"return {expression}")
                self.append_aux_code(('return', '-', '-', expression))
            else:
                self.tac[self.class_name].append(f"return {ctx.VOID().getText()}")
                self.append_aux_code(('return', '-', '-', '-'))


    def visitWhileStatement(self, ctx: yaplParser.WhileStatementContext): #WHILE
        end = self.generate_label()
        while_label = self.generate_label()

        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]

        tac.append(f"{while_label}:")
        temporal = self.visit(ctx.expression()) or ctx.expression().getText()
        tac.append(f"if false {temporal} goto {end}")
        self.append_aux_code(('<-', ctx.expression().getText(), '-', temporal))
        self.append_aux_code(('if false', temporal, '-', end))
        self.visit(ctx.statement())
        tac.append(f"goto {while_label}")
        tac.append(f"{end}")

    def visitClassMethodCallExpression(self, ctx: yaplParser.ClassMethodCallExpressionContext): #LLAMADA A METODO
        method_name = ctx.ID().getText()
        class_name = ctx.expression().getText()

        if self.method_name:
            tac = self.tac[self.class_name][-1][f"{self.class_name}.{self.method_name}:"]
        else:
            tac = self.tac[self.class_name]

        if ctx.expressionList():
            for expression in ctx.expressionList().expression():
                temporal = self.generate_temporal()
                tac.append(f"{temporal} = {expression.getText()}")
                tac.append(f"PUSH PARAM {temporal}")
                

        temporal = self.generate_temporal()
        tac.append(f"{temporal} = CALL {class_name}.{method_name}()")
        if method_name == 'out_int':
            self.append_aux_code(('',))
            self.append_aux_code(('li', '$a0', expression.getText()))
            self.append_aux_code(('li', '$v0', '1'))
            self.append_aux_code(('syscall',))
        else:
            self.append_aux_code(('CALL', method_name, '-', '-'))

            return temporal

    def visitIdentifierExpression(self, ctx: yaplParser.IdentifierExpressionContext): #IDENTIFICADOR

        if ctx.getText() in self.temporal_list:
            if self.type_operation== "assignment":
                return ctx.getText()
            elif self.type_operation== "operation":
                return self.temporal_list[ctx.getText()]

        elif ctx.getText() in self.params:
            for context in self.listener.symbol_table.context:
                if ctx.getText() in context:
                    if context[ctx.getText()]['content'] in self.arguments:
                        return self.arguments[context[ctx.getText()]['content']]

    def get_size(self, type_str): #Obtiene el tamaño de un tipo de dato
        type_sizes = {
            "int": 8,
            "string": 16,
            "bool": 1,
        }
        return type_sizes.get(type_str, 0)



