import tree
from symboltable import SymbolTable

class Scope:
    def __init__(self):
        self.arguments = []
        self.cammands = []
        self.trees = []
        self.symbolTable = SymbolTable()
        self.procedureName = None
    
    def addSTable(self, sysTbl):
        self.symbolTable = sysTbl
    
    def addCommand(self, cmd):
        self.cammands.append(cmd)
    
    def addTree(self, tree):
        self.trees.append(tree)
    
    def rmST(self, st):
        self.symbolTable.remove(st)
    
    def setProcedureName(self, name):
        if self.procedureName == None:
            self.procedureName = name
            self.symbolTable.funcName = name