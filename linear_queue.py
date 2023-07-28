class linqueue:
    def __init__(self):
        # self.list=[0 for i in range(10)]
        self.size=int(input("Enter the size of the queue:"))
        self.front=-1
        self.rear=-1
        self.queue=[0 for i in range(self.size)]
        print(self.queue)
    def enqueue(self,item):
        if self.rear==self.size-1:
            print("Queue is full")
            return
        self.rear+=1
        print('Rear is: ',self.rear)
        self.queue[self.rear]=item
        if self.front==-1:
            self.front=0
            print("front is :",self.front)
        
    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print("Queue is empty")           
            return
        item=self.queue[self.front]
        if self.front==self.rear:          
                self.front=-1
                self.rear=-1
        else:
                self.front+=1
                print('Rear is: ',self.rear)
                print("front is : ",self.front)
        print("Item deleted")        
        return item
    def display(self):
        if self.front==-1 and self.rear==-1:
             print("queue is empty")
             return
        for i in range(self.rear,0):
            print(1)
        for i in range(self.front,self.rear+1):
             print(self.queue[i],end=" ")
ob=linqueue()
while(True):
    print("\n--------------------------")
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
