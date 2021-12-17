
##### Assembly Commands:
from helperFunctions import is_number
#from tree import Tree


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
    list.append('fmtuintin: db "%d", 0')
    list.append('fmtfloatin: db "%f", 0')
    list.append('fmtfloat: db "%g", 10, 0')

    for line in data:
        list.append(line)

def addBssSection(list):
    list.append('section .bss')

    for line in bss:
        list.append(line)

def addTextSection(list):
    list.append('SECTION .text')
    list.append('extern printf')
    list.append('extern scanf')
    list.append('global main')


def printFloat(list, floatName):
    list.append('lea rdi, [fmtfloat]' + ' ;print float')
    list.append('movss xmm0, ' + floatName)
    list.append('cvtss2sd xmm0, xmm0')
    list.append('mov rax, 1')


def printString(list, stringName):
    list.append('mov rsi, ' + stringName + ';print string: ' + stringName)
    list.append('mov rdi, fmtstr')
    list.append('xor rax, rax')
    list.append('call printf')


def printUInt(list, intval):
    '''intval must be a string of a number'''
    list.append(';print uint: ' + intval)
    list.append('mov rsi, [' + intval + ']')
    list.append('mov rdi, [fmtuint]')
    list.append('mov rax, 0')
    list.append('call printf')

def readInt(list, intvar):
    list.append('lea rdi, [fmtuintin]' + ' ;read int ' + intvar)
    list.append('lea rsi, ['+intvar+']')
    list.append('mov rax, 0')
    list.append('call scanf')

def printInt(list, intVar):
    list.append('lea rdi, [fmtuint]' + ' ;print int var ' + intVar)
    list.append('mov rsi, ['+intVar+']')
    list.append('xor rax, rax')
    list.append('call printf')

numPowers = 0
def powerfunct(list, base, exp):
    global numPowers
    list.append('xor rdi, rdi')
    list.append('mov rcx, 1')
    list.append('mov rax, ['+ exp +']')
    list.append('mov rbx, ['+base+']')
    list.append('mov rdx, rax')
    list.append('exp_start' + str(numPowers) + ':')
    list.append('cmp rdi, rdx')
    list.append('jz exp_done' +str(numPowers))
    list.append('imul rcx, rbx')
    list.append('inc rdi')
    list.append('jmp exp_start' +str(numPowers))
    list.append('exp_done'+str(numPowers))
    numPowers += 1


def syscall(list):
    list.append('mov rbx, 0')
    list.append('mov rax, 1')
    list.append('int 0x80')

def add(list, first, second, store):
    if is_number(first):
        list.append('mov rcx, ' +first)
    else:
        list.append('mov rcx, [' + first + "]" )
    if is_number(second):
        list.append('mov rbx, ' +second)
    else:
        list.append('mov rbx, [' + second + ']')
    list.append('add rcx, rbx')
    list.append('mov [' + store +'], rcx')

def sub(list, first, second, store):
    if is_number(first):
        list.append('mov rcx, ' +first)
    else:
        list.append('mov rcx, [' + first + "]" )
    if is_number(second):
        list.append('mov rbx, ' +second)
    else:
        list.append('mov rbx, [' + second + ']')
    list.append('sub rcx, rbx')
    list.append('mov [' + store +'], rcx')

def mul(list, first, second, store):
    if is_number(first):
        list.append('mov rax, ' + first)
    else:
        list.append('mov rax, [' + first + "]" )
    if is_number(second):
        list.append('mov rbx, ' + second)
    else:
        list.append('mov rbx, [' + second + ']')
    list.append('mul rbx')
    list.append('mov [' + store +'], rax')

def div(list, first, second, store):
    if is_number(first):
        list.append('mov rax, ' + first)
    else:
        list.append('mov rax, [' + first + "]" )
    if is_number(second):
        list.append('mov rbx, ' + second)
    else:
        list.append('mov rbx, [' + second + ']')
    list.append('xor rdi, rdi')
    list.append('div rbx')
    list.append('mov [' + store +'], rax')

def copy(list, fromVar, toVar):
    list.append('mov rdx, ['+ fromVar +']')
    list.append('mov [' + toVar +'], rdx')


def loadValues(list, var, number):
    list.append('mov rcx, ' + number + " ;loading value "+ number +" into " + var ) 
    list.append('mov ['+ var + '], rcx')


def procedure(list, scope):
    list.append(scope.procedureName + ": ;" +scope.procedureName + "()")
    list.append('push rax')
    list.append('push rbx')

    for cmd in scope.cammands:
        try:
            if isinstance(cmd, str):
                if 'procedure' in cmd:
                    continue
                if 'printNum' in cmd:
                    cmd = cmd.removeprefix('printNum ')
                    try:
                        printInt(list, cmd)
                    except:
                        continue
                if 'printString' in cmd:
                    cmd = cmd.removeprefix('printString ')
                    printString(list, cmd)
                if 'readNum' in cmd:
                    cmd = cmd.removeprefix('readNum ')
                    readInt(list, cmd)
                if 'return' in cmd:
                    list.append('mov rax, [result]')
            elif cmd.hasVars:
                cmd.traversWithVars(list, cmd.topNode)
        except:
            continue

    list.append('''pop rbx''')
    list.append('''pop rax''')
    list.append('ret')