class node:
    def __init__(self,value):
        self.info=value
        self.link=None
class stackLink:
    def __init__(self):
        self.start=None
        self.top=None
    def push(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
            self.top=n
        else:
            self.top.link=n
            self.top=n
    def pop(self):
        if self.start==None:
            print("Empty stack")
            return -1
        elif self.start==self.top:
            p=self.start
            item=p.info
            self.start=None
            self.top=None
            del p
            print("Item deleted")
            return item
        else:
            p=self.start
            while(p.link!=self.top):
                p=p.link
            p.link=None
            q=self.top
            self.top=p
            item=q.info
            del q
            print("Item deleted")
            return item
            
    def display(self):
        if self.top==None:
            print("Empty stack")
        elif self.start==self.top:
            print(self.start.info)
        else:
            p=self.start
            while(p!=None):
                print(p.info)
                p=p.link
ob=stackLink()
while(True):
    print("--------------------------")
    print("\n******MENU******")
    print(" 1.Push \n 2.Pop \n 3.Display \n 4.Exit")
    ch=int(input("Enter your choice:"))        
    if ch==1:
        ob.push(int(input("\nEnter the value:")))
    elif ch==2:
        ob.pop()
    elif ch==3:
        ob.display()
    elif ch==4:
        break
    else:
        print("Invalid choice")
