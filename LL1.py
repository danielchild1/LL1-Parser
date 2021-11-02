#!/usr/bin/env python3
print('\n\033[91m' + "hello Brad I just " + '\033[1m' + "Learned " + '\033[0m' + '\033[94m' + "how to color the text in\033[93m the \033[4mterminal" + '\033[0m \n' )

from colorama import Fore, Back, Style
from Production import Production
from helperFunctions import *

# l0 = Production(lSide="Goal", f="Expr")
# l1 = Production(lSide="Expr", f="LTerm", s="ExprP")
# l2 = Production(lSide="LTerm", f="LFactor", s="TermP")
# l3 = Production(lSide="RTerm", f="RFactor", s="TermP")
# l4 = Production(lSide="ExprP", f="+", s="RTerm", t="ExprP")
# l5 = Production(lSide="ExprP", f="-", s="RTerm", t="ExprP")
# l6 = Production(lSide="ExprP", f="ε")
# l7 = Production(lSide="TermP", f="*", s="RTerm", t="ExprP")
# l8 = Production(lSide="TermP", f="/", s="RTerm", t="ExprP")
# l9 = Production(lSide="TermP", f="ε")
# l10 = Production(lSlide='LFactor', f='GFactor')
# l11 = Production(lSlide='LFactor', f='negnum') #negative val without space only left term
# l12 = Production(lSlide='LFactor', f='negname') #negative name without space only left term
# l13 = Production(lSlide='RFactor', f='GFactor')
# l14 = Production(lSlide='GFactor', f='(', s="Expr", t=")")
# l15 = Production(lSlide='GFactor', f='PosVal')
# l16 = Production(lSlide='GFactor', f='SpaceNegVal')
# l17 = Production(lSide="PosVal", f="num")
# l18 = Production(lSide="PosVal", f="name")
# l19 = Production(lSide="SpaceNegVal", f="spacenegnum")
# l20 = Production(lSide="SpaceNegVal", f="spacenegname")
# ProList = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20]

l0 = Production(lSide="Goal", f="Expr")
l1 = Production(lSide="Expr", f="Term", s="ExprP")
l2 = Production(lSide="ExprP", f="+", s="Term", t="ExprP")
l3 = Production(lSide="ExprP", f="-", s="Term", t="ExprP")
l4 = Production(lSide='ExprP', f="ε")
l5 = Production(lSide='Term', f="Factor", s="TermP")
l6 = Production(lSide='TermP', f="*", s="Factor", t="TermP")
l7 = Production(lSide="TermP", f="/", s="Factor", t="TermP")
# l8 = Production(lSide="TermP", f="^", s="Factor", t="TermP")
l9 = Production(lSide='TermP', f="ε")
l10 = Production(lSide='Factor', f="(", s="Expr", t=")")
l11 = Production(lSide='Factor', f="num")
l12 = Production(lSide='Factor', f="name")
ProList = [l0, l1, l2, l3, l4, l5, l6, l7, l9, l10, l11, l12]

#FIRST
First = {}
for t in terminals:
    First[t] = t
for a in nonTerminals:
    First[a] = None
tempFirst = First.copy()
changing = True
while changing:
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
    if tempFirst == First:
        changing = False #if it did not change exit while loop
    else:
        tempFirst = First.copy()

print(First['Expr'])
print(First['ExprP'])
print(First['Term'])
print(First['TermP'])
print(First['Factor'])
print(First['num'])
print(First['name'])

exit(0)
# #sudo code on page 112 of textbook
# with open('./tests/invalid.txt')as file:
#     for line in file:
#         line = line.strip()
#         ogLine = line
#         try:
#             word = NextWord(line)
#             line = line.removeprefix(word)

#             stack = []
#             stack.append('eof')
#             stack.append('Goal')
#             focus = stack[len(stack)-1] #focus <- top of stack
#             while True:
#                 if focus == 'eof' and word== 'eof': 
#                     break; #success
#                 elif focus == 'eof' or focus in terminals:
#                     if focus == word2Terminal(word):
#                         stack.pop()
#                         word = NextWord(line)
#                         line = line.removeprefix(" ")
#                         line = line.removeprefix(word)

#                     else:
#                         raise Exception(" looking for symbol at top of stack")
#                 else:
#                     table = parseTable[focus][word2Terminal(word)]
#                     #print(Fore.CYAN + word2Terminal(word)+ " " + str(table))
#                     if table != None:
#                         stack.pop()
#                         regergitatedMess = ProList[table].regurgitate()
#                         for reger in regergitatedMess:
#                             if reger != "ε":
#                                 stack.append(reger)
#                     else:
#                         raise Exception(" not found in parse table")
#                 focus = stack[len(stack)-1]
#         except Exception as e:
#             print(Fore.RED + Back.BLACK+ Style.BRIGHT + "Error:" + Style.NORMAL + " command: " + ogLine +Style.RESET_ALL )
#             continue
#         print(Fore.GREEN + ogLine + Style.RESET_ALL)






