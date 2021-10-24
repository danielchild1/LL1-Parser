import Production

whitespace = Production('<WHITESPACE>','\s')
digit = Production('<DIGIT>', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
number = Production('<NUMBER>', '<DIGIT><BETA>')
beta = Production('<BETA>',  number, 'e')
negNumber = Production('<NEGATIVE NUMBER>', '-<NUMBER>')
posOrNeg = Production('<POS OR NEG>', number, negNumber)
op = Production('<OP>', posOrNeg, '<VARIABLE NAME><REF>')
paren = Production('<PAREN>', '(<EXP>)')
li = Production('<LI>', '<OP>', '<PAREN>')
ri = Production('<RI>', '<WHITESPACE><OP>', '<PAREN>')
ae = Production('<AE>', '+<RI><AE>', '-<RI><AE>','/<RI><AE>','*<RI><AE>','^<RI><AE>', 'e')
exp = Production('<EXP>', '<LI><AE>')
ProList = [whitespace, digit,number,beta,negNumber,posOrNeg,op,paren,li,ri,ae,exp]

def findProduction(name):
    for o in ProList:
        if o.name == name:
            return o



hashTable = {} #nonterminal, index of productionArr

