import re
terminals = ["eof", "+", "-", "*", "/", "(", ")", "name", "num"]
nonTerminals = ['Goal', "Expr", "ExprP", "Term", "TermP", "Factor"]

def word2Terminal(oj):
    if oj in terminals:
        return oj
    else:
        try:
            temp = int(oj)
            if isinstance(temp, int):
                return "num"
            else:
                raise Exception("not an integer")
        except:
            if re.search('^[a-z|A-Z]+[a-z|A-Z|0-9|_]*', oj):
                return "name"


def NextWord(line):
    charList = ["+", "-", "*", "/", "(", ")"]
    word = ""

    if len(line) > 0:
        for c in line:
            if c in charList:
                if len(word) == 0:
                    line.removeprefix(c)
                    return c
                else:
                    line.removeprefix(word)
                    return word
            elif c == " ":
                line.removeprefix(word)
                return word
            else:
                line.removeprefix(word)
                word += c

        line.removeprefix(word)
        return word