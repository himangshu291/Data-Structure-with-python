class operation:
    def __init__(self):
        self.size=int(input("Enter the size:"))
        self.top=-1
        self.stack=[]
    def empty(self):
        if self.stack==[]:
            return True
    def push(self,data):
        if self.top==self.size-1:
            print("Stack is full or overflow")
        else:
            self.top+=1
            self.stack.append(data)
            print("Item is inserted")
    def pop(self):
        if ob.empty():
            print("Underflow or the stack is empty")
        else:
            self.stack.pop()
            print("Item is deleted")
            self.top-=1
    def peek(self):
        if ob.empty():
            print("Stack is empty")
        else:
            return self.stack[self.top]
    
    def display(self):
        if self.top==-1:        #if self.stack==[]:
            print("Stack is empty")
        else:
            print("\nThe items are:")
            for i in range(len(self.stack)):
                print(f"stack[{i}]:",self.stack[i])
ob=operation()
while(True):
    print("--------------------------")
    print("\n******MENU******")
    print(" 1.PUSH\n 2.POP\n 3.DISPLAY\n 4.PEEK\n 5.EXIT")
    ch=int(input("Enter your choice:"))        
    if ch==1:
        ob.push(int(input("\nEnter the item:")))
    elif ch==2:
        ob.pop()
    elif ch==3:
        ob.display()
    elif ch==4:
        res=ob.peek()
        print("Top value is:",res)
    elif ch==5:
        break
    else:
        print("Sorry wrong choice")