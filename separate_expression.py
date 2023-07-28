inf=input("Enter the Expression to separate:")
list=inf.split(" ")
paren=[]
opr=[]
operand=[]
stack=[]
for i in list:
    if i=="(" or i==")":
        paren.append(i)
    elif i=="+" or i=="-" or i=="/" or i=="*" or i=="^" or i=="%":
        opr.append(i)
    elif (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or i.isnumeric():
        operand.append(i) 
print("Parenthesis:",paren)
print("Operators are:",opr)
print("Operands are:",operand)

