class SymbolTable:
    def __init__(self):
        self.map = {}
    
    def Lookup(self, name):
        try:
            return self.map[name]
        except:
            return None
        
    
    def Insert(self, name, record):
        self.map[name] = record
 