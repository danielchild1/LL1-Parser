#!/usr/bin/env python3
print('\n\033[91m' + "hello Brad I just " + '\033[1m' + "Learned " + '\033[0m' + '\033[94m' + "how to color the text in\033[93m the \033[4mterminal" + '\033[0m \n' )
from colorama import Fore, Back, Style
from Production import Production
from helperFunctions import *

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


parseTable = {'Goal': {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 0, ')': None, 'name': 0, 'num':0 },
    'Expr':           {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 1, ')': None, 'name': 1, 'num':1 },
    'ExprP':          {'eof': 4,    '+': 2   , '-': 3   , '*': None, '/': None, '(': None,')': 4, 'name': None, 'num':None},
    'Term':           {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 5, ')': None, 'name': 5, 'num':5 },
    'TermP':          {'eof': 8, '+': 8, '-': 8, '*': 6, '/': 7, '(': None, ')': 8, 'name': None, 'num': None },
    'Factor':         {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 9, ')': None, 'name': 11, 'num':10 }
}



#sudo code on page 112 of textbook
with open('./tests/valid.txt')as file:
    for line in file:
        line = line.strip()
        ogLine = line
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
                        stack.pop()
                        word = NextWord(line)
                        line = line.removeprefix(" ")
                        line = line.removeprefix(word)

                    else:
                        raise Exception(" looking for symbol at top of stack")
                else:
                    table = parseTable[focus][word2Terminal(word)]
                    #print(Fore.CYAN + word2Terminal(word)+ " " + str(table))
                    if table != None:
                        stack.pop()
                        regergitatedMess = ProList[table].regurgitate()
                        for reger in regergitatedMess:
                            if reger != "ε":
                                stack.append(reger)
                    else:
                        raise Exception(" not found in parse table")
                focus = stack[len(stack)-1]
        except Exception as e:
            print(Fore.RED + Back.BLACK+ Style.BRIGHT + "Error:" + Style.NORMAL + " command: " + ogLine +Style.RESET_ALL )
            continue
        print(Fore.GREEN + ogLine + Style.RESET_ALL)






