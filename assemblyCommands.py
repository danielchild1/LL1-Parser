##### Assembly Commands:
data = []
bss = []

def add2DataSection(line):
    data.append(line)

def add2BssSection(line):
    bss.append(line)

def addDataSection(list):
    list.append('SECTION .data')
    list.append('fmtstr: db "%s", 10, 0')
    list.append('fmtuint: db "%d", 10, 0')
    list.append('fmtfloatin: db "%f", 0')
    list.append('fmtfloat: db "%g", 10, 0')


    for line in data:
        list.append(line)

def printFloat(list, floatName):
    list.append(';print float')
    list.append('lea rdi, fmtfloat')
    list.append('movss xmm0, ' + floatName)
    list.append('cvtss2sd xmm0, xmm0')
    list.append('mov rax, 1')


def printString(list, stringName):
    list.append(';print string: ' + stringName)
    list.append('mov rsi, ' + stringName)
    list.append('mov rdi, fmtstr')
    list.append('mov rax, 0')
    list.append('call printf')


def printUInt(list, intval):
    '''intval must be a string of a number'''
    list.append(';print uint: ' + intval)
    list.append('mov rsi, ' + intval)
    list.append('mov rdi, fmtuint')
    list.append('mov rax, 0')
    list.append('call printf')


def syscall(list):
    list.append('mov rbx, 0')
    list.append('move rax, 1')
    list.append('int 0x80')