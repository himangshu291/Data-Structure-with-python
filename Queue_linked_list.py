class node:
    def __init__(self,value):
        self.info=value
        self.link=None
class queueLink:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,value):
        n=node(value)
        if self.rear==None and self.front==None:
            self.front=n
            self.rear=n
        else:
            self.rear.link=n
            self.rear=n
    def dequeue(self):
        if self.rear==None and self.front==None:
            print("Empty queue")
        elif self.front==self.rear:
            p=self.front
            item=p.info
            self.front=None
            self.rear=None
            del p
            print("Item deleted")
            return item
        else:
            p=self.front
            item=p.info
            self.front=p.link
            del p
            print("Item deleted")
            return item
            
    def display(self):
        if self.rear==None and self.front==None:
            print("Empty queue")
        elif self.front==self.rear:
            print(self.front.info)
        else:
            p=self.front
            while(p!=None):
                print(p.info)
                p=p.link
ob=queueLink()
while(True):
    print("--------------------------")
    print("\n******MENU******")
    print(" 1.Enqueue \n 2.Dequeue \n 3.Display \n 4.Exit")
    ch=int(input("Enter your choice:"))        
    if ch==1:
        ob.enqueue(int(input("\nEnter the value:")))
    elif ch==2:
        ob.dequeue()
    elif ch==3:
        ob.display()
    elif ch==4:
        break
    else:
        print("Invalid choice")
