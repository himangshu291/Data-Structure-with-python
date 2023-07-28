class expression:
    def __init__(self):
        stack=[]
        operator={'(','+','-','*','/','^'}
        exp=input("Enter the space separated postfix expression:").split(' ')
        for i in exp:
            if i in operator:
                ele1=int(stack.pop())
                ele2=int(stack.pop())
                if(i=='+'):
                    ele=ele2+ele1
                elif(i=='-'):
                    ele=ele2-ele1
                elif(i=='*'):
                    ele=ele2*ele1
                elif(i=='/'):
                    ele=ele2/ele1
                elif(i=='^'):
                    ele=ele2^ele1
                stack.append(str(ele))
            else:
                stack.append(i)  
        print("postfix Expression:",exp)
        print("Infix Expression:",stack[0])
    
ob=expression()


