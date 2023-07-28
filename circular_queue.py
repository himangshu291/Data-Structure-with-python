class cirqueue:
    def __init__(self):
        # self.list=[0 for i in range(10)]
        self.size=int(input("Enter the size of the queue:"))
        self.front=-1
        self.rear=-1
        self.queue=[0]*self.size
        
    def enqueue(self,item):
        if self.front==0 and self.rear==self.size-1 or self.front==self.rear+1:
            print("Queue is full or overflow")
            return
        elif self.front==-1:
            self.front=self.rear=0
        elif self.rear==self.size-1:
            self.rear=0
        else:
            self.rear=self.rear+1    
        self.queue[self.rear]=item
        print("Item inserted")
        print("rear is : ",self.rear) 
        print("front is : ",self.front)       
        
    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print("Queue is empty or underflow")           
            return
        item=self.queue[self.front]
        if self.front==self.rear:          
            self.front=self.rear=-1
        elif self.front==self.size-1:
            self.front=0    
        else:
            self.front+=1
        print("Item deleted")
        print("rear is : ",self.rear) 
        print("front is : ",self.front)        
        return item
    
    def display(self):
        if self.front==-1 and self.rear==-1:
             print("queue is empty")
             return
        if self.rear>=self.front:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
        else:
            for i in range(self.front,self.size+1):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
ob=cirqueue()
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
