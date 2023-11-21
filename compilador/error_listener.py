from antlr4.error.ErrorListener import ErrorListener
from symbol_table  import SymbolTable
from grammar.yaplLexer import yaplLexer
class ErrorListenerC(ErrorListener):
    def __init__ (self):
        self.errors =[]
        self.symbol_table = SymbolTable()
    
    def sintax_errors(self, line, col, lexer_msg, is_instance):

        if isinstance(is_instance, yaplLexer):
            err = lexer_msg.split("'")[1]
            self.errors.append(
                f"ERROR léxico en línea {line}, columna {col}: Carácter inesperado -> '{err}'")
        
