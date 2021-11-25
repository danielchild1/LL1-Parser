nonTerminals = ["Goal", "LineFull", "VarTypeAfter", "LineVarName", "LineVarNameRemaining", "ProcedureParams", "Params", "MoreParams", "VarType", "Expr", "LTermAddSub", "LTermMultDiv", "RTermAddSub", "RTermMultDiv", "AddSubP", "MultDivP", "MultAndRightOp", "DivAndRightOp", "powerP", "PowerAndRightOp", "LTermPower", "RTermPower", "GTerm", "Parens", "PosVal", "SpaceNegVal", 'return', '=', 'ε', 'PowerP']
terminals = ["eof", "+", "-", "*", "/", "^", "(", ")", "name", "num", "spacenegnum", 'spacenegname', "negnum", "negname", "ε", "{", "}", ",", "ish", "result", "procedure", 'negnum_value', 'negish_value', 'num_value', 'ish_value', 'spacenegnum_value', 'spacenegish_value']
nonOperatorTerminals = ["eof", "(", ")", "name", "num", "spacenegnum", 'spacenegname', "negnum", "negname", "ε", "{", "}", ",", "ish", "result", "procedure"]
operators = ["+", "-", "*", "/", "^"]
# nonTerminals = ['Goal', "Expr", "LTerm", "RTerm", "ExprP", "TermP", "LFactor", "RFactor", "GFactor", "PosVal", "SpaceNegVal"]
ronts = ["RTermAddSub", "RTermMulTDiv", "RTermPower"]

# terminals = ['eof', '+', '-', '*', '/', "(", ")", "name", "num", "ε"]
# nonTerminals = ['Goal', 'Expr', 'ExprP', 'Term', "TermP", "Factor"]

# parseTable = {'Goal': {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 0, ')': None, 'name': 0, 'num':0 },
#     'Expr':           {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 1, ')': None, 'name': 1, 'num':1 },
#     'ExprP':          {'eof': 4,    '+': 2   , '-': 3   , '*': None, '/': None, '(': None,')': 4, 'name': None, 'num':None},
#     'Term':           {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 5, ')': None, 'name': 5, 'num':5 },
#     'TermP':          {'eof': 8, '+': 8, '-': 8, '*': 6, '/': 7, '(': None, ')': 8, 'name': None, 'num': None },
#     'Factor':         {'eof': None, '+': None, '-': None, '*': None, '/': None, '(': 9, ')': None, 'name': 11, 'num':10 }
# }


from os import fwalk
import re
regNum = re.compile(r'^[0-9]+.?[0-9]*$')
regName = re.compile(r'^[a-z|A-Z]+[a-z|A-Z|0-9|_]*$')
regspacenegnum = re.compile(r'^\s-[0-9]+.?[0-9]*$')
regspacenegname = re.compile(r'^\s-[a-z|A-Z]+[a-z|A-Z|0-9|_]*$')
regnegnum = re.compile(r'^-[0-9]+.?[0-9]*$')
regnegname = re.compile(r'^-[a-z|A-Z]+[a-z|A-Z|0-9|_]*$')
def word2Terminal(oj):
    if oj in terminals:
        return oj
    else:
        if regName.match(oj):
            return "name"
        if regNum.match(oj):
            return "num"
        if regspacenegname.match(oj):
            return "spacenegname"
        if regspacenegnum.match(oj):
            return "spacenegnum"
        if regnegname.match(oj):
            return "negname"
        if regnegnum.match(oj):
            return "negnum"



def NextWord(line, lastWordWasANumberVarOrRightparens=False):
    charList = ["+", "-", "*", "/", "(", ")", "^"]
    word = ""
    numNonSpaceChars = 0
    numSpaceChars = 0

    if len(line) > 0:
        #for c, cf in zip(line, line[1:]+[None]):
        for i, c in enumerate(line):
            cf = None
            if len(line) > (i+1):
                cf = line[i+1]
            if c in charList:
                if numNonSpaceChars > 0:
                    break
                if c == '(':
                    return '('
                if c == '-':
                    if lastWordWasANumberVarOrRightparens == False: # and regNum.match(cf) if the enxt word is a diget or regName.match(cf)
                        word += c
                        numNonSpaceChars += 1
                        continue
                    else:
                        return '-'
                if numNonSpaceChars == 0 and numSpaceChars == 0:
                    line = line.removeprefix(c)
                    return c
                else:
                    if cf == " ":
                        return c

                    word += c   
            elif c == " " and len(word) > 0 and numNonSpaceChars > 0:
                line = line.removeprefix(word)
                break
            else:
                if c != " ":
                    numNonSpaceChars += 1
                else:
                    numSpaceChars += 1
                word += c

        if '-' in word:
            while numSpaceChars > 1:
                word = word.removeprefix(" ")
                numSpaceChars -= 1
        else:
            word = word.removeprefix(' ')

        line = line.removeprefix(word)
        return word
    else:
        return 'eof'


def onion(first, second):
    ret = []

    if isinstance(first, list):
        for i in first:
            if i != None and i not in ret:
                ret.append(i)
    else:
        if first != None:
            ret.append(first)


    if isinstance(second, list):
        for j in second:
            if j != None and j not in ret:
                ret.append(j)
    else:
        if second != None and second not in ret:
            ret.append(second)


    # if len(ret) == 0:
    #     return None
    # elif len(ret) ==1:
    #     return ret[0]

    return ret


def subEpsolon(p):
    if isinstance(p, list):
        newList = []
        for l in p:
            if l != "ε":
                newList.append(l)
        return newList

    if p == "ε":
        return None
    else:
        return p



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

# l0 = Production(lSide="Goal", f="Expr")
# l1 = Production(lSide="Expr", f="LTerm", s="ExprP")
# l2 = Production(lSide="LTerm", f="LFactor", s="TermP")
# l3 = Production(lSide="RTerm", f="RFactor", s="TermP")
# l4 = Production(lSide="ExprP", f="+", s="RTerm", t="ExprP")
# l5 = Production(lSide="ExprP", f="-", s="RTerm", t="ExprP")
# l6 = Production(lSide="ExprP", f="ε")
# l7 = Production(lSide="TermP", f="*", s="RFactor", t="TermP")
# l8 = Production(lSide="TermP", f="/", s="RFactor", t="TermP")
# l8p2 = Production(lSide="TermP", f="^", s="RFactor", t="TermP")
# l9 = Production(lSide="TermP", f="ε")
# l10 = Production(lSide='LFactor', f='GFactor')
# l11 = Production(lSide='LFactor', f='negnum') #negative val without space only left term
# l12 = Production(lSide='LFactor', f='negname') #negative name without space only left term
# l13 = Production(lSide='RFactor', f='GFactor')
# l14 = Production(lSide='GFactor', f='(', s="Expr", t=")")
# l15 = Production(lSide='GFactor', f='PosVal')
# l16 = Production(lSide='GFactor', f='SpaceNegVal')
# l17 = Production(lSide="PosVal", f="num")
# l18 = Production(lSide="PosVal", f="name")
# l19 = Production(lSide="SpaceNegVal", f="spacenegnum")
# l20 = Production(lSide="SpaceNegVal", f="spacenegname")
# ProList = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l8p2, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20]