SECTION .data
fmtstr: db "%s", 10, 0
fmtuint: db "%d", 10, 0
fmtuintin: db "%d", 0
fmtfloatin: db "%f", 0
fmtfloat: db "%g", 10, 0
s0: db "This begins the user input section", 0
s1: db "Supply data and hit enter", 0
s2: db "Enter a number: ", 0
s3: db "Result of adding first and second user inputs: ", 0
s4: db "Result of multiplying third and fourth user inputs: ", 0
s5: db "Enter a radius: ", 0
s6: db "The volume is: ", 0
s7: db "Congratulations on the great semester!", 0
section .bss
var1: resd 1 
var2: resd 1 
var3: resd 1 
var4: resd 1 
var5: resd 1 
var6: resd 1 
var7: resd 1 
var8: resd 1 
var9: resd 1 
var10: resd 1 
var11: resd 1 
var12: resd 1 
var14: resd 1 
var15: resd 1 
var16: resd 1 
var17: resd 1 
var18: resd 1 
var19: resd 1 
var20: resd 1 
var21: resd 1 
var22: resd 1 
var24: resd 1 
var25: resd 1 
var26: resd 1 
var28: resd 1 
var29: resd 1 
var30: resd 1 
var31: resd 1 
var32: resd 1 
var33: resd 1 
var34: resd 1 
var35: resd 1 
var36: resd 1 
var37: resd 1 
var39: resd 1 
var40: resd 1 
var41: resd 1 
var42: resd 1 
var43: resd 1 
var44: resd 1 
var45: resd 1 
float1: resd 1 
float2: resd 1 
float3: resd 1 
float4: resd 1 
issue1: resd 1 
issue2: resd 1 
orig: resd 1 
user1: resd 1 
user2: resd 1 
user3: resd 1 
user4: resd 1 
result1: resd 1 
a: resd 1 
b: resd 1 
userRadius: resd 1 
SECTION .text
extern printf
extern scanf
global main
main: 
mov rcx, 12 ;loading value 12 into var1
mov [var1], rcx
mov rcx, 2 ;loading value 2 into var2
mov [var2], rcx
mov rcx, 2 ;loading value 2 into var3
mov [var3], rcx
mov rcx, 17 ;loading value 17 into var4
mov [var4], rcx
mov rcx, 1542 ;loading value 1542 into var5
mov [var5], rcx
mov rcx, 0 ;loading value 0 into var6
mov [var6], rcx
mov rcx, 29 ;loading value 29 into var7
mov [var7], rcx
mov rcx, 42 ;loading value 42 into var8
mov [var8], rcx
mov rcx, 42 ;loading value 42 into var9
mov [var9], rcx
mov rcx, 42 ;loading value 42 into var10
mov [var10], rcx
mov rcx, 42 ;loading value 42 into var11
mov [var11], rcx
mov rcx, 7006652 ;loading value 7006652 into var12
mov [var12], rcx
mov rcx, 10 ;loading value 10 into var14
mov [var14], rcx
mov rcx, 9 ;loading value 9 into var15
mov [var15], rcx
mov rcx, 31 ;loading value 31 into var16
mov [var16], rcx
mov rcx, 123 ;loading value 123 into var17
mov [var17], rcx
mov rcx, -42 ;loading value -42 into var18
mov [var18], rcx
mov rcx, -42 ;loading value -42 into var19
mov [var19], rcx
mov rcx, -42 ;loading value -42 into var20
mov [var20], rcx
mov rcx, -42 ;loading value -42 into var21
mov [var21], rcx
mov rcx, 8 ;loading value 8 into var22
mov [var22], rcx
mov rcx, 2 ;loading value 2 into var24
mov [var24], rcx
mov rcx, 2 ;loading value 2 into var25
mov [var25], rcx
mov rcx, 5 ;loading value 5 into var26
mov [var26], rcx
mov rcx, 1 ;loading value 1 into var28
mov [var28], rcx
mov rcx, -2 ;loading value -2 into var29
mov [var29], rcx
mov rcx, -2 ;loading value -2 into var30
mov [var30], rcx
mov rcx, -2 ;loading value -2 into var31
mov [var31], rcx
mov rcx, 1 ;loading value 1 into var32
mov [var32], rcx
mov rcx, 1 ;loading value 1 into var33
mov [var33], rcx
mov rcx, -2 ;loading value -2 into var34
mov [var34], rcx
mov rcx, -2 ;loading value -2 into var35
mov [var35], rcx
mov rcx, -2 ;loading value -2 into var36
mov [var36], rcx
mov rcx, -2 ;loading value -2 into var37
mov [var37], rcx
mov rcx, -2 ;loading value -2 into var39
mov [var39], rcx
mov rcx, 11 ;loading value 11 into var40
mov [var40], rcx
mov rcx, 27 ;loading value 27 into var41
mov [var41], rcx
mov rcx, 256 ;loading value 256 into var42
mov [var42], rcx
mov rcx, 19683 ;loading value 19683 into var43
mov [var43], rcx
mov rcx, 19683 ;loading value 19683 into var44
mov [var44], rcx
mov rcx, 41 ;loading value 41 into var45
mov [var45], rcx
mov rcx, 3 ;loading value 3 into float1
mov [float1], rcx
mov rcx, 3 ;loading value 3 into float2
mov [float2], rcx
mov rcx, 3 ;loading value 3 into float3
mov [float3], rcx
mov rcx, 5 ;loading value 5 into float4
mov [float4], rcx
mov rcx, 5 ;loading value 5 into issue1
mov [issue1], rcx
mov rcx, 7 ;loading value 7 into issue2
mov [issue2], rcx
mov rcx, 6 ;loading value 6 into orig
mov [orig], rcx
mov rcx, 0 ;loading value 0 into user1
mov [user1], rcx
mov rcx, 0 ;loading value 0 into user2
mov [user2], rcx
mov rcx, 0 ;loading value 0 into user3
mov [user3], rcx
mov rcx, 0 ;loading value 0 into user4
mov [user4], rcx
mov rcx, 3 ;loading value 3 into result1
mov [result1], rcx
mov rcx, 2 ;loading value 2 into a
mov [a], rcx
mov rcx, 3 ;loading value 3 into b
mov [b], rcx
mov rcx, 0 ;loading value 0 into userRadius
mov [userRadius], rcx
lea rdi, [fmtuint] ;print int var var1
mov rsi, [var1]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var2
mov rsi, [var2]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var3
mov rsi, [var3]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var4
mov rsi, [var4]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var5
mov rsi, [var5]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var6
mov rsi, [var6]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var7
mov rsi, [var7]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var8
mov rsi, [var8]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var9
mov rsi, [var9]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var10
mov rsi, [var10]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var11
mov rsi, [var11]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var12
mov rsi, [var12]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var14
mov rsi, [var14]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var15
mov rsi, [var15]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var16
mov rsi, [var16]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var17
mov rsi, [var17]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var18
mov rsi, [var18]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var19
mov rsi, [var19]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var20
mov rsi, [var20]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var21
mov rsi, [var21]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var22
mov rsi, [var22]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var24
mov rsi, [var24]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var25
mov rsi, [var25]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var26
mov rsi, [var26]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var28
mov rsi, [var28]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var29
mov rsi, [var29]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var30
mov rsi, [var30]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var31
mov rsi, [var31]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var32
mov rsi, [var32]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var33
mov rsi, [var33]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var34
mov rsi, [var34]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var35
mov rsi, [var35]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var36
mov rsi, [var36]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var37
mov rsi, [var37]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var39
mov rsi, [var39]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var40
mov rsi, [var40]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var41
mov rsi, [var41]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var42
mov rsi, [var42]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var43
mov rsi, [var43]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var44
mov rsi, [var44]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var var45
mov rsi, [var45]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var orig
mov rsi, [orig]
xor rax, rax
call printf
mov rsi, "This begins the user input section";print string: "This begins the user input section"
mov rdi, [fmtstr]
mov rax, 0
call printf
mov rsi, "Supply data and hit enter";print string: "Supply data and hit enter"
mov rdi, [fmtstr]
mov rax, 0
call printf
mov rsi, "Enter a number: ";print string: "Enter a number: "
mov rdi, [fmtstr]
mov rax, 0
call printf
lea rdi, [fmtuint] ;print int var user1
mov rsi, [user1]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var user2
mov rsi, [user2]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var user3
mov rsi, [user3]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var user4
mov rsi, [user4]
xor rax, rax
call printf
lea rdi, [fmtuint] ;print int var result1
mov rsi, [result1]
xor rax, rax
call printf
mov rsi, "Result of adding first and second user inputs: ";print string: "Result of adding first and second user inputs: "
mov rdi, [fmtstr]
mov rax, 0
call printf
mov rsi, "Result of multiplying third and fourth user inputs: ";print string: "Result of multiplying third and fourth user inputs: "
mov rdi, [fmtstr]
mov rax, 0
call printf
mov rsi, "Enter a radius: ";print string: "Enter a radius: "
mov rdi, [fmtstr]
mov rax, 0
call printf
mov rsi, "The volume is: ";print string: "The volume is: "
mov rdi, [fmtstr]
mov rax, 0
call printf
mov rsi, "Congratulations on the great semester!";print string: "Congratulations on the great semester!"
mov rdi, [fmtstr]
mov rax, 0
call printf
mov rbx, 0
mov rax, 1
int 0x80
