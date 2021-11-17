class Node:
    def __init__(self, operator):
        self.left = None
        self.right = None
        self.operator = operator
    
    def __str__(self):
        return self.production
    
    def __len__(self):
        size = 0
        if self.left != None:
            size += 1
        if self.right != None:
            size += 1
        return size


#Left
#Right operand
#operator

