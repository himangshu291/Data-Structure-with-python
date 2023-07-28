class expression:
    def __init__(self):
        res=[]
        stack=[]
        precedence={'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}
        top=-1
        exp=input("Enter the space separated infix expression:")
        for i in exp:
            if i=='(':
                stack.append(i)
            elif i==')':
                while(stack[top]!='('):
                    res.append(stack.pop())
                stack.pop()
            elif i=='+' or i=='-' or i=='*' or i=='/' or i=='^':
                if(len(stack)>0):
                    while(precedence[stack[top]]>=precedence[i]):
                        res.append(stack.pop())
                        if(len(stack)==0):
                            break
                stack.append(i)
            else:
                res.append(i)  
        while(len(stack)!=0):
            res.append(stack.pop())
        # print("Infix Expression:",exp)
        print("Postfix Expression:",end=' ')
        for i in res:
            print(i,end='')
ob=expression()


