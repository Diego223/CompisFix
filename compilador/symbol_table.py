class SymbolTable:
    def __init__(self):
        self.context = [{}]

    def in_context(self):
        self.context.append({})

    def out_context(self):
        if len(self.context) > 1 and self.context[-1] == {}:
            self.context.pop()


    
    def get_symbol_in_context(self, symbol):
        for context in reversed(self.context):
            if symbol in context:
                return context[symbol]
        return None


    def create_symbol(self, symbol, type, line=None, column=None):
        if symbol not in self.context[-1]:
            
            self.context[-1][symbol] = {'type': type, 'line': line, 'column': column}
        return None
    

    def is_symbol_created(self, symbol, current_context=False):
        if current_context:
            return symbol in self.context[-1] 
        return any(symbol in context for context in self.context) 
    
