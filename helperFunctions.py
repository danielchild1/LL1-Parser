import re
terminals = ["eof", "+", "-", "*", "/", "(", ")", "name", "num"]
nonTerminals = ['Goal', "Expr", "ExprP", "Term", "TermP", "Factor"]
regNum = re.compile(r'^[0-9]+')
regName = re.compile(r'^[a-z|A-Z]+[a-z|A-Z|0-9|_]*')
parseTable = {'Goal': {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 0, ')': None, 'name': 0, 'num':0 },
    'Expr':           {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 1, ')': None, 'name': 1, 'num':1 },
    'ExprP':          {'eof': 4,    '+': 2   , '-': 3   , '*': None, '/': None, '(': None,')': 4, 'name': None, 'num':None},
    'Term':           {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 5, ')': None, 'name': 5, 'num':5 },
    'TermP':          {'eof': 8, '+': 8, '-': 8, '*': 6, '/': 7, '(': None, ')': 8, 'name': None, 'num': None },
    'Factor':         {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 9, ')': None, 'name': 11, 'num':10 }
}



def word2Terminal(oj):
    if oj in terminals:
        return oj
    else:
        if regName.match(oj):
            return "name"
        if regNum.match(oj):
            return "num"



def NextWord(line):
    charList = ["+", "-", "*", "/", "(", ")"]
    word = ""

    if len(line) > 0:
        for c in line:
            if c in charList:
                if len(word) == 0:
                    line = line.removeprefix(c)
                    return c
                else:
                    line = line.removeprefix(word)
                    return word
            elif c == " " and len(word) > 0:
                line = line.removeprefix(word)
                return word
            else:
                if c != " ":
                    word += c

        line = line.removeprefix(word)
        return word
    else:
        return 'eof'



# l0 = Production(lSide="Goal", f="Expr")
# l1 = Production(lSide="Expr", f="Term", s="ExprP")
# l2 = Production(lSide="ExprP", f="+", s="Term", t="ExprP")
# l3 = Production(lSide="ExprP", f="-", s="Term", t="ExprP")
# l4 = Production(lSide='ExprP', f="ε")
# l5 = Production(lSide='Term', f="Factor", s="TermP")
# l6 = Production(lSide='TermP', f="*", s="Factor", t="TermP")
# l7 = Production(lSide="TermP", f="/", s="Factor", t="TermP")
# # l8 = Production(lSide="TermP", f="^", s="Factor", t="TermP")
# l9 = Production(lSide='TermP', f="ε")
# l10 = Production(lSide='Factor', f="(", s="Expr", t=")")
# l11 = Production(lSide='Factor', f="num")
# l12 = Production(lSide='Factor', f="name")
# ProList = [l0, l1, l2, l3, l4, l5, l6, l7, l9, l10, l11, l12]