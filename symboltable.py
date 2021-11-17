class SymbolTable:
    def __init__(self):
        self.map = {}
    
    def Lookup(self, name):
        return self.map[name]
    
    def Insert(self, name, record):
        self.map[name] = record
 