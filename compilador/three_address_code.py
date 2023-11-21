from grammar.yaplListener import yaplListener
from grammar.yaplParser import yaplParser
from grammar.yaplVisitor import yaplVisitor
from symbol_table import SymbolTable
import re

class tac_listener (yaplListener):

    def __init_(self, errors):
        self.symbol_table = SymbolTable()
        self.errors = errors
        self.is_in_block = False
        self.class_name = None
        self.method_type = None
        self.method_params = None
        self.is_main_class = False
    # creacion de symbols 
    def create_symbol(self, ctx, type, symbol):
        if type: 
            if self.symbol_table.is_symbol_created(symbol):
                for header, content in self.method_params.items(): 
                    if symbol in content['params']:
                        self.errors.errors = []
                        self.symbol_table.create_symbol(symbol, type, ctx.start.line, ctx.start.column)
                    else:
                        self.errors.errors.append(f'{symbol} ya ha sido declarado')
            else :
                self.errors.errors = []
                self.symbol_table.create_symbol(symbol, type, ctx.start.line, ctx.start.column)
        else: 
            if not self.symbol_table.is_symbol_created(symbol, current_context= True): 
                self.errors.errors.append(f'{symbol} esta en uso y no ha sido declarado')

    def set_access(self, ctx, symbol):
        if not self.symbol_table.is_symbol_created(symbol):
            self.errors.errors.append(f"{symbol} que no ha sido declarado.")
        else:
            self.symbol_table.get_symbol_in_context(symbol)['accessed'] = True
   
    def enterProgram (self, ctx : yaplParser.ProgramContext):
        pass

    def exitProgram (self, ctx : yaplParser.ProgramContext):
        is_main_class_declared = False
        is_main_method_declared = False

        for context in self.symbol_table.context:
            for header, content in context.items():
                if header == 'Main': 
                    is_main_class_declared = True
                    self.is_main_class = True
                elif header == 'main': 
                    is_main_method_declared = True
            

        if not is_main_method_declared or not is_main_class_declared:
            self.errors.errors.append(f'No se ha declarado la clase Main o el metodo main()')

    
    def enterClassDeclaration(self, ctx: yaplParser.ClassDeclarationContext):
        self.symbol_table.in_context() 
        basic_classes= ['IO', 'String', 'Object']
        class_name = ctx.TYPE_ID()[0].getText() 
        self.create_symbol(ctx, 'class', class_name)
        self.class_name = class_name
    
        if ctx.TYPE_ID()[1]: 
            inherits = ctx.TYPE_ID()[1].getText()
            if class_name == "Main" and (inherits not in basic_classes):
                self.errors.errors.append(f'La clase Main unicamente puede heredar de las clases basicas')
            elif class_name in basic_classes:
                self.errors.errors.append(f'La clase no puede llamarse como las clases basicas ')
            
            if inherits in basic_classes: #https://theory.stanford.edu/~aiken/software/cool/cool-manual.pdf
                if inherits == 'IO': 
                    self.create_symbol(ctx, type= '(method)self', symbol='out_string')
                    self.method_params['out_string'] = {
                                                            'type' : 'self',
                                                            'params' : {'x': 'string'}
                                                        }
                    self.create_symbol(ctx, type= '(method)self', symbol='out_int')
                    self.method_params['out_int'] = {
                                                            'type' : 'self',
                                                            'params' : {'x': 'int'}
                                                        }
                    
                    self.create_symbol(ctx, type= '(method)int', symbol='in_int')
                    self.create_symbol(ctx, type= '(method)string', symbol='in_string')

                elif inherits == 'String':
                     
                    
                    self.create_symbol(ctx, '(method)string', 'concat')
                    self.method_params['concat'] = {
                                                            'type': 'string', 
                                                            'params': {"s": 'string'}
                                                    }
                    self.create_symbol(ctx, type= '(method)string', symbol='substr')
                    self.method_params['substr'] = {
                                                            'type': 'string', 
                                                            'params': {'i': 'int', 'e': 'int'}
                                                    }
                    self.create_symbol(ctx, 'int', 'length')
                elif inherits == 'Object':
                    self.create_symbol(ctx, type='(method)self', symbol='copy')
                    self.create_symbol(ctx, type='(method)string', symbol='type_name')
                    self.create_symbol(ctx, type='(method)Object', symbol= 'abort')
            elif not self.symbol_table.is_symbol_created(inherits):
                self.errors.errors.append(f'{inherits} no esta declarado como una clase')

        
    def exitClassDeclaration(self, ctx: yaplParser.ClassDeclarationContext):
        self.symbol_table.out_context() 
        
    def enterMethodDeclaration(self, ctx: yaplParser.MethodDeclarationContext):
        self.symbol_table.in_context() 
        method_name = ctx.ID().getText()
        method_type = ctx.getChild(0).getText()
        params = ctx.parameterList() 
        self.method_type = method_type 
        self.create_symbol(ctx, type= '(method)'+ method_type, symbol= method_name)  
        self.method_params[method_name] =    { 
                                    'type' : method_type,
                                    'params' : {}
                                }
        if params:
            for p in params.parameter():
                param_type = p.getChild(0).getText()
                param_name = p.ID().getText()
                self.method_params[method_name]['params'][param_name] = param_type 
                self.create_symbol(ctx, type=param_type, symbol=param_name)
            
    def exitMethodDeclaration(self, ctx: yaplParser.MethodDeclarationContext):
        self.method_type = ''
    
    def enterMethodCallStatement(self, ctx: yaplParser.MethodCallStatementContext):
        method_name = ctx.ID().getText()
        params = ctx.expressionList()
        if self.symbol_table.is_symbol_created(method_name):
            if '(method)' in self.symbol_table.get_symbol_in_context(method_name):
                if self.symbol_table.is_symbol_created(method_name)['type'] != '(method)self':
                    if method_name in self.method_params:
                        if self.method_params[method_name]['params'].isEmpty():
                            if params:
                                self.errors.errors.append(f'el metodo {method_name} no esta declarado con parametros')
                        elif params:
                            for param in params.expression():
                                if param.ID():
                                    param_name = param.ID().getText()
                                    param_type = self.symbol_table.get_symbol_in_context(param_name)['type']
                                    for header, content in self.method_params[method_name]['params'].items():
                                        if param_name == header or param_type == self.method_params[method_name]['params'][header]:
                                            for scope in self.symbol_table.scopes:
                                                if method_name in scope:
                                                    if header in scope:
                                                        scope[header]['valor'] = param_name
                                        else:
                                            self.errors.errors.append(f"El parametro declarado no es del tipo correcto")
                                    if param_name and self.method_params[method_name]['params']:
                                        self.errors.errors.append(f"El método {method_name} no requiere parámetros.")
                                if param.getText()[0] == '"' and param.getText()[-1] == '"':
                                     for header, content in self.method_params[method_name]['params'].items():
                                        if content != 'string':
                                            self.errors.errors.append(
                                                f"Parametro esta declarado como tipo string")
                                if param.getText().isnumeric():
                                    for header, content in self.method_params[method_name]['params'].items():
                                        if content == 'int':
                                            for context in self.symbol_table.context:
                                                if method_name in context:
                                                    if header in context:
                                                        context[header]['content'] = param.getText()
                                                        context[header]['accessed'] = True
                                        else:
                                            self.errors.errors.append(
                                                f"Parametro esta declarado como tipo int")
                    
                                if 'true' in param.getText() or 'false' in param.getText():
                                    for header, content in self.method_params[method_name]['params'].items():
                                        if content != "bool":
                                            
                                            self.errors.errors.append(f'parametro declarado como tipo BOOL')
                        else :
                            self.errors.errors.append(f'el metodo {method_name} requiere parametros') 

        else:
            self.errors.errors.append(f'metodo {method_name} no declarado')                    
                    
    def exitMethodCallStatement(self, ctx: yaplParser.MethodCallStatementContext):
        pass

    def enterClassMethodCallExpression(self, ctx: yaplParser.ClassMethodCallExpressionContext):
        
        expression = ctx.expression().getText()
        symbol = ctx.ID().getText()
        if self.symbol_table.is_symbol_created(expression, current_context = True):
            expression_type = self.symbol_table.get_symbol_in_context(expression)['type']
            if self.symbol_table.is_symbol_created(expression_type):
                pass
            elif expression_type == 'string':
                if symbol == "length":
                    pass
                elif symbol == "concat":
                    pass
                    
                    if ctx.expressionList():
                        for param in ctx.expressionList().expression():
                            param_name = param.getText()
                            
                            if self.symbol_table.is_symbol_created(param_name):
                                param_type = self.symbol_table.get_symbol_in_context(param_name)['type']
                                if param_type == 'string':
                                    pass
                                else:
                                    self.errors.errors.append(
                                        f"El metodo {symbol} requiere parametros string")
                            else:
                                if param_name.startswith('"') and param_name.endswith('"'):
                                    pass
                                else:
                                    self.errors.errors.append(
                                        f"El método {symbol} requiere parámetros de tipo string")
                elif symbol == "substr":
                    
                    if ctx.expressionList():
                        for param in ctx.expressionList().expression():
                            param_name = param.getText()
                            
                            if self.symbol_table.is_symbol_created(param_name):
                                param_type = self.symbol_table.get_symbol_in_context(param_name) ['type']
                                if param_type == 'int':
                                    pass
                                else:
                                    self.errors.errors.append(
                                        f"El método {symbol} requiere parámetros de tipo int")
                            else:
                                if param_name.isnumeric():
                                    pass
                                else:
                                    self.errors.errors.append(
                                        f"El método <{symbol}> requiere parámetros de tipo <int>.")
                else:
                    self.errors.errors.append(
                        f"{symbol} no es un método de la clase {expression_type}.")

            else:
                self.errors.errors.append(
                    f"{expression_type} no es una clase que ha sido declarada.")

    def exitClassMethodCallExpression(self, ctx: yaplParser.ClassMethodCallExpressionContext):
        pass

    def enterBlock(self, ctx: yaplParser.BlockContext):
        self.is_in_block = True
        if ctx.LBRACE().getText() != "{":
            self.errors.errors.append("'{' <- Hace falta ")

    def exitBlock(self, ctx: yaplParser.BlockContext):
        self.is_in_block = False
        if ctx.RBRACE().getText() != "}":
            self.errors.errors.append("'}' <- Hace falta")
   
    def enterVariableDeclaration(self, ctx: yaplParser.VariableDeclarationContext):
        if self.is_in_block :  
            variable_name = ctx.ID().getText()
            variable_type = ctx.getChild(0).getText()  
            self.create_symbol(ctx, type=type, symbol= variable_name)
        else: 
            variable_name = ctx.type_().getText()
            variable_type = ctx.ID().getText()
            if ctx.statement():
                expression = ctx.statement().getText()
                if expression.isnumeric() and variable_type != 'int':
                    self.errors.errors.append( f"Se le está asignando un valor de tipo int a un tipo {variable_type}")
                elif (expression[0] == '"' and expression[-1] == '"') and variable_type != 'string':
                    self.errors.errors.append(f"Se le está asignando un valor de tipo string a un tipo {variable_type}")
                elif (expression == 'true' or expression == 'false') and variable_type != "bool":
                    self.errors.errors.append(f"Se le está asignando un valor de tipo bool a un tipo {variable_type}")
                else:
                    self.create_symbol(ctx, variable_type, variable_name)

    def exitVariableDeclaration(self, ctx: yaplParser.VariableDeclarationContext):
        if self.is_in_block:  
            pass


    def enterAttributeDeclaration(self, ctx: yaplParser.AttributeDeclarationContext):
        attribute = ctx.ID().getText()
        attribute_type = ctx.getChild(0).getText()
        self.create_symbol(ctx, attribute_type, attribute)

    def exitAttributeDeclaration(self, ctx: yaplParser.AttributeDeclarationContext):
        pass


    def enterAssignmentDeclaration(self, ctx: yaplParser.AssignmentDeclarationContext):
        
        symbol = ctx.ID().getText()
        self.set_access(ctx, symbol)

    def exitAssignmentDeclaration(self, ctx: yaplParser.AssignmentDeclarationContext):
        pass

    def enterIfStatement(self, ctx: yaplParser.IfStatementContext):
        expression = ctx.expression().getText()
        bool_operators = [ '!=', '<', '==', '<=', '>','>=']
        for operator in bool_operators:
            if operator in expression:
                operation = re.split(operator, expression)
                if operator in bool_operators:
                    if self.symbol_table.is_symbol_created(operation[0]): 
                        if self.symbol_table.is_symbol_created(operation[1]): 
                            if self.symbol_table.get_symbol_in_context(operation[0])['type'] != self.symbol_table.get_symbol_in_context(operation[1])['type']:
                            
                                self.errors.errors.append(
                                    f"las variables deben de ser del mismo tipo para ser comparadas")
                        elif operation[1].isnumeric():
                            if self.symbol_table.get_symbol_in_context(operation[0])['type'] != 'int':
            
                                self.errors.errors.append(f"la operacion debe de contener el mismo tipo de variables para ser comparada")
                        elif operation[1].startswith('"') and operation[1].endswith('"'):
                            if self.symbol_table.get_symbol_in_context(operation[0])['type'] != 'string':
                               
                                self.errors.errors.append(f"la operacion debe de contener el mismo tipo de variables para ser comparada")
                        elif operation[1] == 'true' or operation[1] == 'false':

                            if self.symbol_table.get_symbol_in_context(operation[0])['tipo'] != "bool":
                        
                                self.errors.errors.append(f"la operacion debe de contener el mismo tipo de variables para ser comparada")
                        else:
                            self.errors.errors.append(f"uso de variables no declaradas")
                
    def exitIfStatement(self, ctx: yaplParser.IfStatementContext):
        pass
