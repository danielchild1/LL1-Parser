from colorama import Fore, Back, Style
from helperFunctions import terminals, nonOperatorTerminals, nonTerminals, operators, ronts
class Node:
    nodeid = 0
    def __init__(self, operator=None):
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
#all three ways: https://1533221.mediaspace.kaltura.com/media/CS+6820+Nov+8+2021/1_lxrr725p

class Tree:
    def __init__(self, operator=None):
        try:
            self.nodePointers = []
            self.integerStack = []
            self.topNode = Node(operator)
            self.traversalStack = []
            self.erroredOut = False
            self.varName = None
            self.stringgg = " "
            if operator == None:
                self.numNodes = -1
            else:
                self.numNodes = 1
            self.currNode = self.topNode
        except:
            self.errorMessage("could not init object. operator=" + operator)
    
    def __len__(self):
        try:
            return self.numNodes
        except:
            self.errorMessage("error in len. (Good thing I added this)")
    
    def topStackNode(self):
        return self.nodePointers[len(self.nodePointers)-1]

    def goLeft(self):
        try:
            self.nodePointers.append(self.topStackNode().left)
            self.currNode = self.currNode.left
        except:
            self.errorMessage("problem in goLeft()")
    
    def goRight(self):
        try:
            self.nodePointers.append(self.topStackNode().right)
            self.currNode = self.currNode.left
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
                self.goRight()
        except:
            self.errorMessage("exception thrown in addNodeRight() operator="+operator+" move="+move)

    def addParent(self, operator):
        try:
            newparent = Node(operator)
            newparent.left = self.topNode
            self.topNode = newparent
            self.numNodes += 1
            self.nodePointers.insert(0,newparent)
        except:
            self.errorMessage("exception thrown in addParent() operator="+operator)
    
    def addParent2current(self, operator):
        try:
            if self.currNode == self.topNode:
                self.addParent(operator)
            else:

                newNode = Node(operator)

                parentNode = self.nodePointers[len(self.nodePointers)-2]
                parentNode.right = parentNode.left
                parentNode.left = newNode
                newNode.left = self.currNode
                self.currNode = newNode
                self.currNode.right = Node()
                self.currNode = self.currNode.right
                
                self.nodePointers.pop()
                self.nodePointers.append(parentNode.left)
                self.nodePointers.append(parentNode.left.right)
                self.numNodes += 1


        except:
            self.errorMessage("exception thrown in addParent2current() operator="+operator)
    
    def poppedOffTheStack(self, stackObject, word, wholeStack): #todo: might need to use this word
        try:

            if stackObject in terminals or stackObject == 'eof':

                if stackObject in nonOperatorTerminals:

                    if self.numNodes == -1:
                        newNode = Node(word)
                        self.numNodes = 1
                        self.topNode = newNode
                        self.currNode = self.topNode
                        self.nodePointers = [self.topNode]

                    elif word != ')':
                        self.currNode.operator = word

                elif stackObject in operators:
                    if self.currNode == self.topNode:
                        self.addParent(stackObject)
                        self.currNode = self.topNode
                        self.nodePointers = [self.topNode]
                        self.currNode.right = Node()
                        self.currNode = self.currNode.right
                        self.nodePointers.append(self.currNode)
                    else:
                        self.addParent2current(stackObject)
            if stackObject in nonTerminals:

                if len(self.integerStack) > 0:
                    if len(wholeStack)+1 == self.integerStack[len(self.integerStack)-1]:
                        self.returnCurrNodeFocusToParrent()
                        self.integerStack.pop()
           

        except:
            self.errorMessage("Exception thrown in poppedOffTheStack(). stackObject=" + stackObject)
            self.erroredOut = True
    
    def addRONT(self, placeHolder, index):
        '''Next, this code must remember when this RONT’s full usage through the parsing is done, or in 
            other words, when the right operand is done.  The best way to do this is that just prior to 
            consuming the RONT on the stack, record the stack’s size and push that value in a second stack 
            which holds integer values'''
        try:
            newNode = Node(placeHolder)
            self.currNode.right = newNode
            self.currNode = self.currNode.right
            self.integerStack.append(index)
        except:
             self.errorMessage("Excpetion thrown in addPlaceHolder(). placeHolder=" + placeHolder)
    
    def returnCurrNodeFocusToParrent(self):
        try:
            if len(self.nodePointers) > 1:
                self.nodePointers.pop()
            self.currNode = self.nodePointers[len(self.nodePointers)-1]
        except:
            self.errorMessage("Excpetion thrown in returnCurrNodeFocusToParrent")

    def postOrderTraversal(self, node):
        try:

            if node.left != None:
                self.postOrderTraversal(node.left)
            if node.right != None:
                self.postOrderTraversal(node.right)

            if node.operator in operators:
                val1 = self.traversalStack.pop()
                val2 = self.traversalStack.pop()

                val1 = int(float(val1))
                val2 = int(float(val2)) 
                if node.operator == '+':
                    self.traversalStack.append(str(val1+val2))
                if node.operator == '-':
                    self.traversalStack.append(str(val2-val1))
                if node.operator == '*':
                    self.traversalStack.append(str(val1*val2))
                if node.operator == '/':
                    if val1 == 0:
                        raise("divide by zero")
                    self.traversalStack.append(str(val2/val1))
                if node.operator == '^':
                    self.traversalStack.append(str(val2**val1))
            
            else:
                if node.operator not in ['(', ')']:
                    self.traversalStack.append(node.operator)
                
        except:
            self.errorMessage("Excpetion thrown in postOrderTraversal()")
    
    def printTraversal(self, node):
        
        if node.left != None:
            self.printTraversal(node.left)
        if node.right != None:
            self.printTraversal(node.right)

        if node.operator not in ['(', ')']:
            self.stringgg += node.operator + ' '

    def errorMessage(self, message):
        debug_mode = False
        if debug_mode:
            print(Fore.YELLOW + Style.BRIGHT + "Error: " + Style.NORMAL + message + Style.RESET_ALL)