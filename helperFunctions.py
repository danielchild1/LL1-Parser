nonTerminals = ["Goal", "LineFull", "VarTypeAfter", "LineVarName", "LineVarNameRemaining", "ProcedureParams", "Params", "MoreParams", "VarType", "Expr", "LTermAddSub", "LTermMultDiv", "RTermAddSub", "RTermMultDiv", "AddSubP", "MultDivP", "MultAndRightOp", "DivAndRightOp", "PowerAndRightOp", "LTermPower", "RTermPower", "GTerm", "Parens", "PosVal", "SpaceNegVal", 'PowerP', 'ExprWithoutName', 'Condition', 'NameOrProcedure', 'Arguments', 'MoreArguments']
terminals = ["eof", "+", "-", "*", "/", "^", "(", ")", '=', '==', '!=', 'ε', "name", "num", 'spacenegname', "negnum", "negname", "{", "}", ",", "ish", "procedure", 'negnum_value', 'negish_value', 'num_value', 'ish_value', 'spacenegnum_value', 'spacenegish_value', 'return', 'printNum', 'printIsh', 'readNum', 'readIsh', 'printString', 'sstring']
nonOperatorTerminals = ["eof", "(", ")", '=', '==', '!=', 'ε', "name", "num", 'spacenegname', "negnum", "negname", "{", "}", ",", "ish", "procedure", 'negnum_value', 'negish_value', 'num_value', 'ish_value', 'spacenegnum_value', 'spacenegish_value', 'return', 'printNum', 'printIsh', 'readNum', 'readIsh', 'printString', 'sstring']
operators = ["+", "-", "*", "/", "^"]
# nonTerminals = ['Goal', "Expr", "LTerm", "RTerm", "ExprP", "TermP", "LFactor", "RFactor", "GFactor", "PosVal", "SpaceNegVal"]
ronts = ["RTermAddSub", "RTermMulTDiv", "RTermPower"]

# terminals = ['eof', '+', '-', '*', '/', "(", ")", "name", "num", "ε"]
# nonTerminals = ['Goal', 'Expr', 'ExprP', 'Term', "TermP", "Factor"]

import re
import sys
regspacenegish_val = re.compile(r'^\s-[0-9]+.[0-9]*$')
regnegish_val = re.compile(r'^-[0-9]+.[0-9]*$')
regish_val = re.compile(r'^\s?[0-9]+.[0-9]*$')

regnegnum_value = re.compile(r'^-[0-9]+$')
regspaecnegnum_value = re.compile(r'^\s-[0-9]+$')
regnum_value = re.compile(r'^\s?[0-9]+$')

regName = re.compile(r'^[a-z|A-Z]+[a-z|A-Z|0-9|_]*$')
regspacenegname = re.compile(r'^\s-[a-z|A-Z]+[a-z|A-Z|0-9|_]*$')
regnegname = re.compile(r'^-[a-z|A-Z]+[a-z|A-Z|0-9|_]*$')

regSTRING = re.compile(r'^\".*\"$')

def word2Terminal(oj):
    if oj in terminals:
        return oj
    else:
        if regName.match(oj):
            return "name"
        if regish_val.match(oj):
            return "ish_value"
        if regspacenegname.match(oj):
            return "spacenegname"
        if regspacenegish_val.match(oj):
            return "spacenegish_value"
        if regnegname.match(oj):
            return "negname"
        if regnegish_val.match(oj):
            return "negish_value"
        if regnegnum_value.match(oj):
            return "negnum_value"
        if regspaecnegnum_value.match(oj):
            return "spacenegnum_value"
        if regnum_value.match(oj):
            return "num_value"
        if regSTRING.match(oj):
            return "sstring"


def nextwordisastring(line):
    retrunString = ''
    openQuoteFound = False
    for l in line:
        if openQuoteFound and l != '"':
            retrunString += l
        elif openQuoteFound and l == '"':
            retrunString += '"'
            return retrunString
        elif openQuoteFound == False and l == '"':
            retrunString += l
            openQuoteFound = True
    return '"Oops somehow the nextwordisastring() function didnt work"'



def NextWord(line, lastWordWasANumberVarOrRightparens=False):
    charList = ["+", "-", "*", "/", "(", ")", "^", ',']
    word = ""
    numNonSpaceChars = 0
    numSpaceChars = 0
    isString = False

    if len(line) > 0:
        #for c, cf in zip(line, line[1:]+[None]):
        for i, c in enumerate(line):
            cf = None

            if c == ',' and numNonSpaceChars > 0:
                break

            if c == '"':
                return nextwordisastring(line)
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

def TOP(list):
    return list[len(list)-1]

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


if __name__ =="__main__":
    print(NextWord('    "lets go get tacos"', False))
    print(sys.version_info)
    print(word2Terminal('printNum'))
    assert(sys.version_info[0] == 3 and sys.version_info[1] >= 9)


