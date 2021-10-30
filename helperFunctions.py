import re
terminals = ["eof", "+", "-", "*", "/", "(", ")", "name", "num"]
nonTerminals = ['Goal', "Expr", "ExprP", "Term", "TermP", "Factor"]
regNum = re.compile(r'^[0-9]+')
regName = re.compile(r'^[a-z|A-Z]+[a-z|A-Z|0-9|_]*')
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
                line = line.removeprefix(c)
                return word
            else:
                word += c

        line = line.removeprefix(word)
        return word
    else:
        return 'eof'