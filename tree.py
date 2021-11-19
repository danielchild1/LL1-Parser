from colorama import Fore, Back, Style
class Node:
    nodeid = 0
    def __init__(self, operator):
        self.nodeID = Node.nodeid
        Node.nodeid += 1
        self.left = None
        self.right = None
        self.operator = operator
    
    def __str__(self):
        return self.operator
    
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

#helpFul lecture video: https://1533221.mediaspace.kaltura.com/media/CS%206820%20Nov%203%202021/1_j3e7nuyw

class Tree:
    def __init__(self, operator=None):
        try:
            self.topNode = Node(operator)
            self.numNodes = 0
            self.currNode = self.topNode
        except:
            self.errorMessage("could not init object. operator=" + operator)
    
    def __len__(self):
        try:
            return self.numNodes
        except:
            self.errorMessage("error in len. (Good thing I added this)")
        

    def goLeft(self):
        try:
            self.currNode = self.currNode.left
        except:
            self.errorMessage("problem in goLeft()")
    
    def goRight(self):
        try:
            self.currNode = self.currNode.right
        except:
            self.errorMessage("problem in goRight()")

    def addNodeLeft(self, operator, move=False):
        try:
            self.currNode.left = Node(operator)
            self.numNodes += 1
            if move:
                self.goLeft()
        except:
            self.errorMessage("exception thrown in addNodeLeft() operator="+operator+" move="+move)
    
    def addNodeRight(self, operator, move=False):
        try:
            self.currNode.right = Node(operator)
            self.numNodes += 1
            if move:
                self.goRight
        except:
            self.errorMessage("exception thrown in addNodeRight() operator="+operator+" move="+move)

    def addParent(self, operator):
        try:
            newparent = Node(operator)
            newparent.left = self.topNode
            self.topNode = newparent
            self.currNode += 1
        except:
            self.errorMessage("exception thrown in addParent() operator="+operator)
    
    def addParent2current(self, operator):
        try:
            if self.currNode == self.topNode:
                self.addParent(operator)
            else:
                newNode = Node(operator)
                newNode.left = self.currNode.left
                self.currNode.left = newNode
                self.currNode += 1

        except:
            self.errorMessage("exception thrown in addParent2current() operator="+operator)
    
    def errorMessage(self, message):
        print(Fore.YELLOW + Style.BRIGHT + "Error: " + Style.NORMAL + message + Style.RESET_ALL)