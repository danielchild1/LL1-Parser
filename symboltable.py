class SymbolTable:
    def __init__(self):
        self.map = {}
        self.treeMap = {}
        self.funcName = None
    
    def Lookup(self, name):
        try:
            return self.map[name]
        except:
            return None
    
    def remove(self, name):
        if name in self.map:
            self.map.pop(name)
        if name in self.treeMap:
            self.map.pop(name)
    
    def Insert(self, name, record=None):
        if name not in self.map:
            self.map[name] = record
        else:
            raise Exception('var "' + name + '" already defined')
    
    def update(self, name, record):
        self.map[name] = record
    
    def addTree(self, name, tree):
        self.treeMap[name] = tree
 