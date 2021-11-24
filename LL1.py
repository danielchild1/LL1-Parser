#!/usr/bin/env python3
print('\n\033[91m' + "hello Brad I just " + '\033[1m' + "Learned " + '\033[0m' + '\033[94m' + "how to color the text in\033[93m the \033[4mterminal" + '\033[0m \n' )


from colorama import Fore, Back, Style
from Production import Production
from helperFunctions import *
from pprint import pprint

try:
    testString = " 343 343 343 343 "
    testString = testString.removeprefix(" ")
    testString = testString.removesuffix("343 ")
except:
    print(Fore.RED + Back.LIGHTBLACK_EX + Style.BRIGHT + "Error: " + Style.NORMAL + "you are not using python >= 3.9" + Style.RESET_ALL)
    exit(2)

l0 = Production(lSide="Goal", f="Expr")
l1 = Production(lSide="Expr", f="LTerm", s="ExprP")
l2 = Production(lSide="LTerm", f="LFactor", s="TermP")
l3 = Production(lSide="RTerm", f="RFactor", s="TermP")
l4 = Production(lSide="ExprP", f="+", s="RTerm", t="ExprP")
l5 = Production(lSide="ExprP", f="-", s="RTerm", t="ExprP")
l6 = Production(lSide="ExprP", f="ε")
l7 = Production(lSide="TermP", f="*", s="RFactor", t="TermP")
l8 = Production(lSide="TermP", f="/", s="RFactor", t="TermP")
l8p2 = Production(lSide="TermP", f="^", s="RFactor", t="TermP")
l9 = Production(lSide="TermP", f="ε")
l10 = Production(lSide='LFactor', f='GFactor')
l11 = Production(lSide='LFactor', f='negnum') #negative val without space only left term
l12 = Production(lSide='LFactor', f='negname') #negative name without space only left term
l13 = Production(lSide='RFactor', f='GFactor')
l14 = Production(lSide='GFactor', f='(', s="Expr", t=")")
l15 = Production(lSide='GFactor', f='PosVal')
l16 = Production(lSide='GFactor', f='SpaceNegVal')
l17 = Production(lSide="PosVal", f="num")
l18 = Production(lSide="PosVal", f="name")
l19 = Production(lSide="SpaceNegVal", f="spacenegnum")
l20 = Production(lSide="SpaceNegVal", f="spacenegname")
ProList = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l8p2, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20]


#FIRST
First = {}
for t in terminals:
    First[t] = t
for a in nonTerminals:
    First[a] = None
Firstlastiteration = First.copy()
while True:
    for i, p in enumerate(ProList):
        
        rhs = []
        rhs.extend(onion(subEpsolon(First[p.productions[0]]), None))

        i = 1
        for i, b in enumerate(p.productions):
            if b == "ε" and i+1 <= len(p.productions)-1:
                rhs = onion(rhs, subEpsolon(First[p.productions[i+1]]))
                i += 1
        
        if p.getLastPro() == "ε" and len(p.productions) == 1:
            rhs.append("ε")
        
        First[p.lSide] = onion(First[p.lSide], rhs)
    
    #did First change at all?
    if Firstlastiteration == First:
        break #if it did not change exit while loop
    else:
        Firstlastiteration = First.copy()



#FOLLOW
Follow = {}

for a in nonTerminals:
    Follow[a] = None

Follow[l0.lSide] = 'eof'
FollowLastIteration = Follow.copy()
while True:

    for i, p in enumerate(ProList):
        Trailer = Follow[p.lSide]

        for i in p.productions[::-1]:
            if i in nonTerminals:
                Follow[i] = onion(Follow[i], Trailer)

                if "ε" in First[i]:
                    Trailer = onion(Trailer, subEpsolon(First[i]))
                else:
                    Trailer = First[i]
            
            else:
                Trailer = First[i]



    if FollowLastIteration == Follow:
        break
    else:
        FollowLastIteration = Follow.copy()


#First+
def firstPlus(prod):
    if "ε" in First[prod.productions[0]]:
        return onion(First[prod.productions[0]], Follow[prod.lSide])
    else:
        if isinstance(First[prod.productions[0]], str):
            lst = []
            lst.append(First[prod.productions[0]])
            return lst
        else:
            return First[prod.productions[0]]

#Build Parse Table
parseTable = {}
for A in nonTerminals:
    for W in terminals:
        parseTable[A, W] = None

    for i, p in enumerate(ProList):
        if p.lSide == A:
            fp = firstPlus(p)
            for w in fp:
                if parseTable[A, w] == None:
                    parseTable[A, w] = i
            if 'eof' in firstPlus(p) and parseTable[A, 'eof'] == None:
                parseTable[A, 'eof'] = i

#pprint(parseTable)


from tree import Tree
treeList = []
ronts = ['RTerm', 'RFactor']


    # needRont = tree.poppedOffTheStack(itemPopedOff, word)
    # if needRont:
    #     tree.addRONT(stack[len(stack)-1],len(stack)-1)
    #     lastItemWasARont = True
    # # if needRont == False and lastItemWasARont == True:
    # #     lastItemWasARont = False
    # elif needRont == False and lastItemWasARont == False:
    #     if len(stack) == tree.integerStack[len(tree.integerStack)-1]:
    #         tree.integerStack.pop()
    #         tree.returnCurrNodeFocusToParrent()

#simple binary tree LL1 parser
#sudo code on page 112 of textbook
with open('./tests/valid.txt')as file:
    for line in file:
        line = line.strip()
        ogLine = line
        lastWordWasANumberVarOrRightparens = False
        tree = Tree()
        try:
            word = NextWord(line)
            line = line.removeprefix(word)

            stack = []
            stack.append('eof')
            stack.append('Goal')
            focus = stack[len(stack)-1] #focus <- top of stack
            while True:
                if focus == 'eof' and word== 'eof': 
                    break; #success
                elif focus == 'eof' or focus in terminals:
                    if focus == word2Terminal(word):
                        word = NextWord(line, lastWordWasANumberVarOrRightparens)

                        #NEW ASSIGNMENT CODE
                        itemPopedOff = stack.pop()
                        needRont = tree.poppedOffTheStack(itemPopedOff, word)
                        if needRont:
                            tree.addRONT(stack[len(stack)-1],len(stack)-1)
                        if itemPopedOff not in operators and itemPopedOff not in ronts:
                            if len(stack) == tree.integerStack[len(tree.integerStack)-1]:
                                tree.integerStack.pop()
                                tree.returnCurrNodeFocusToParrent()
                        #END NEW ASSIGNMENT CODE
                        
                        line = line.removeprefix(" ")
                        line = line.removeprefix(word)

                    else:
                        raise Exception(" looking for symbol at top of stack")
                else:
                    table = parseTable[focus,word2Terminal(word)]
                    if table != None:

                        #NEW ASSIGNMENT CODE
                        itemPopedOff = stack.pop()
                        needRont = tree.poppedOffTheStack(itemPopedOff, word)
                        if needRont:
                            tree.addRONT(stack[len(stack)-1],len(stack)-1)
                        if itemPopedOff not in operators and itemPopedOff not in ronts:
                            if len(stack) == tree.integerStack[len(tree.integerStack)-1]:
                                tree.integerStack.pop()
                                tree.returnCurrNodeFocusToParrent()
                        #END NEW ASSIGNMENT CODE


                        regergitatedMess = ProList[table].regurgitate()
                        for reger in regergitatedMess:
                            if reger != "ε":
                                stack.append(reger)
                    else:
                        raise Exception(" not found in parse table")
                nameNumList = ["name", "num", "spacenegname", "spacenegnum", "negname", "negnum", ")"]
                if word2Terminal(word) in nameNumList:
                    lastWordWasANumberVarOrRightparens = True
                else:
                    lastWordWasANumberVarOrRightparens = False
                focus = stack[len(stack)-1]
        except Exception as e:
            print(Fore.RED + Back.BLACK+ Style.BRIGHT + "Error:" + Style.NORMAL + " command: " + ogLine +Style.RESET_ALL )
            continue
        print(Fore.GREEN + ogLine + Style.RESET_ALL)
        treeList.append(tree)


exit(0)



