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

l0 = Production(lSide="Goal", f="LineFull")
l1 = Production(lSide="LineFull", f="VarType", s="VarTypeAfter")
l2 = Production(lSide="LineFull", f="LineVarName")
l3 = Production(lSide="LineFull", f="negnum", s="PowerP", t="MultDivP", o="AddSubP")
l4 = Production(lSide="LineFull", f="Parens", s="PowerP", t="MultDivP", o="AddSubP")
l5 = Production(lSide="LineFull", f="return", s="GTerm")
l6 = Production(lSide="LineFull", f="}")
l7 = Production(lSide="VarTypeAfter", f="LineVarName")
l8 = Production(lSide="VarTypeAfter", f="procedure", s="name", t="ProcedureParams", o="{")
l9 = Production(lSide="LineVarName", f="name", s="LineVarNameRemaining")
l10 = Production(lSide="LineVarNameRemaining", f='=', s='Expr')
l11 = Production(lSide="LineVarNameRemaining", f='PowerAndRightOp', s='MultDivP', t='AddSubP')
l12 = Production(lSide="LineVarNameRemaining", f='MultAndRightOp', s='AddSubP')
l13 = Production(lSide="LineVarNameRemaining", f='DivAndRightOp', s='AddSubP')
l14 = Production(lSide="LineVarNameRemaining",  f='AddSubP')
l15 = Production(lSide='ProcedureParams', f='(', s='Params', t=')')
l16 = Production(lSide='Params', f='VarType', s='name', t='MoreParams')
l17 = Production(lSide='Params', f='ε')
l18 = Production(lSide='MoreParams', f=",", s='VarType', t='name', o='MoreParams')
l19 = Production(lSide='MoreParams', f='ε')
l20 = Production(lSide='VarType', f='num')
l21 = Production(lSide='VarType', f='ish')
l22 = Production(lSide='Expr', f='LTermAddSub', s='AddSubP')
l23 = Production(lSide='LTermAddSub', f='LTermMultDiv', s='MultDivP')
l24 = Production(lSide='LTermMultDiv', f='LTermPower', s='PowerP')
l25 = Production(lSide='RTermAddSub', f='RTermMultDiv', s='MultDivP')
l26 = Production(lSide='RTermMultDiv', f='RTermPower', s='PowerP')
l27 = Production(lSide='AddSubP', f="+", s='RTermAddSub', t='AddSubP')
l28 = Production(lSide='AddSubP', f="-", s='RTermAddSub', t='AddSubP')
l29 = Production(lSide='AddSubP', f='ε')
l30 = Production(lSide='MultDivP', f='MultAndRightOp')
l31 = Production(lSide='MultDivP', f='DivAndRightOp')
l32 = Production(lSide='MultDivP', f='ε')
l33 = Production(lSide='MultAndRightOp', f="*", s='RTermMultDiv', t='MultDivP')
l34 = Production(lSide='DivAndRightOp', f="/", s='RTermMultDiv', t='MultDivP')
l35 = Production(lSide='PowerP', f='PowerAndRightOp')
l36 = Production(lSide='PowerP', f='ε')
l37 = Production(lSide='PowerAndRightOp', f="^", s='RTermPower', t='PowerP')
l38 = Production(lSide='LTermPower', f='GTerm')
l39 = Production(lSide='LTermPower', f='negnum_value')
l40 = Production(lSide='LTermPower', f='negish_value')
l41 = Production(lSide='LTermPower', f='negname')
l42 = Production(lSide='RTermPower', f='GTerm')
l43 = Production(lSide='GTerm', f='Parens')
l44 = Production(lSide='GTerm', f='PosVal')
l45 = Production(lSide='GTerm', f='SpaceNegVal')
l46 = Production(lSide='Parens', f='(', s='Expr', t=')')
l47 = Production(lSide='PosVal', f='num_value')
l48 = Production(lSide='PosVal', f='ish_value')
l49 = Production(lSide='PosVal', f='name')
l50 = Production(lSide='SpaceNegVal', f='spacenegnum_value')
l51 = Production(lSide='SpaceNegVal', f='spacenegish_value')
l52 = Production(lSide='SpaceNegVal', f='spacenegname')

ProList = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l23, l24, l25, l26, l27, l28, l29, l30, l31, l32, l33, l34, l35, l36, l37, l38, l39, l40, l41, l42, l43, l44, l45, l46, l47, l48, l49, l50, l51, l52]


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

pprint(First)

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


# outputString = ''
# for p in parseTable:
#     for r in parseTable[p]:
#         outputString += r
#     print(outputString)
#     outputString == ''

exit(0)
from tree import Tree
treeList = []


#simple binary tree LL1 parser
#sudo code on page 112 of textbook
with open('./tests/irassignment.txt')as file:
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

                        #NEW ASSIGNMENT CODE
                        tree.poppedOffTheStack(stack.pop(), word, stack)
                        
                        word = NextWord(line, lastWordWasANumberVarOrRightparens)
                        line = line.removeprefix(" ")
                        line = line.removeprefix(word)

                    else:
                        raise Exception(" looking for symbol at top of stack")
                else:
                    table = parseTable[focus,word2Terminal(word)]
                    if table != None:

                        #NEW ASSIGNMENT CODE
                        tree.poppedOffTheStack(stack.pop(), word, stack)



                        regergitatedMess = ProList[table].regurgitate()
                        for reger in regergitatedMess:
                            if reger != "ε":
                                if reger in operators:
                                    tree.integerStack.append(len(stack)-1)
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


#Post Order Traversal
#GO LEFT
#Go RIGHT
#DO Operand 
# for tree in treeList:
#     tempNode



exit(0)


