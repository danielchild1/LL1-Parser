import tree
import symboltable

class Scope:
    def __init__(self):
        self.cammands = []
        self.trees = []
        self.symbolTable = None
    
    def addSTable(self, sysTbl):
        self.symbolTable = sysTbl
    
    def addCommand(self, cmd):
        self.cammands.append(cmd)
    
    def addTree(self, tree):
        self.trees.append(tree)