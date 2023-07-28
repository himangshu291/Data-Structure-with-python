class node:
    def __init__(self,value):
        self.info=value
        self.link=None     
class clinked:
    def __init__(self):
        self.start=None
    def insert_at_beginning(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
            n.link=self.start
        else:
            p=self.start
            self.start=n
            n.link=p
            s=p
            while p.link!=s:
                p=p.link
            p.link=self.start
            
    def insert_at_end(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
        else:
            p=self.start
            while p.link!=self.start:
                p=p.link
            p.link=n
            n.link=self.start
            
    def insert_at_specified_position(self,pos,value):
        n=node(value)
        if self.start==None:
            self.start=n
        else:
            i=1
            p=self.start
            while i<pos and p.link!=self.start:
                prev=p
                p=p.link
                i+=1
            prev.link=n
            n.link=p
            
    def insert_after_specified_item(self,item,value):
        n=node(value)
        if self.start==None:
            self.start=n
        else:
            p=self.start
            while p.info!=item:
                p=p.link
            n.link=p.link
            p.link=n
            
    def delete_start_node(self):
        if self.start==None:
            print("Empty Linked List")
        else:
            p=self.start
            self.start=p.link
            s=p
            while p.link!=s:
                p=p.link
            p.link=self.start
            item=p.info
            del s
            return item
        
    def delete_last_node(self):
        if self.start==None:
            print("Empty Linked List")
        else:
            p=self.start
            while p.link!=self.start:
                prev=p
                p=p.link
            item=p.info
            prev.link=self.start
            del p
            return item
        
    def delete_at_specified_pos_node(self,pos):
        if self.start==None:
            print("Empty Linked List")
        else:
            i=1
            p=self.start
            while i<pos:
                prev=p
                p=p.link
                i+=1
            item=p.info
            prev.link=self.start
            del p
            return item
    
    def delete_node_after_specified_item(self,item):
        if self.start==None:
            print("Empty Linked List")
        else:
            p=self.start
            while p.info!=item:
                p=p.link 
            if p.link==self.start:
                print("There is no node after specified item")
            else:
                t=p.link
                item=t.info
                p.link=self.start
                del p
                return item
        
    def display(self):
        if self.start==None:
            print("Empty Linked List")
            return
        else:
            p=self.start
            print("Nodes of singly linked list:")
            while(p!=None and p.link!=self.start):
                print(p.info,end=" ")
                p=p.link
            print(p.info)
    
ob=clinked()
while(True):
    print("--------------------------")
    print("\n******MENU******")
    print(" 1.insert_at_beginning \n 2.insert_at_end \n 3.insert_at_specified_position \n 4.insert_after_specified_item \n 5.delete_start_node \n 6.delete_last_node \n 7.delete_at_specified_pos_node \n 8.delete_node_after_specified_item \n 9.Display \n 10.EXIT")
    ch=int(input("Enter your choice:"))        
    if ch==1:
        ob.insert_at_beginning(int(input("\nEnter the value:")))
    elif ch==2:
        ob.insert_at_end(int(input("\nEnter the value:")))
    elif ch==3:
        pos=int(input("\nEnter the position:"))
        value=int(input("\nEnter the value:"))
        ob.insert_at_specified_position(pos,value)
    elif ch==4:
        item=int(input("\nEnter the item:"))
        value=int(input("\nEnter the value:"))
        ob.insert_after_specified_item(item,value)
    elif ch==5:
        ob.delete_start_node()
    elif ch==6:
        ob.delete_last_node() 
    elif ch==7:
        ob.delete_at_specified_pos_node(int(input("\nEnter the position:")))
    elif ch==8:
        ob.delete_node_after_specified_item(int(input("\nEnter the value:")))
    elif ch==9:
        ob.display()
    elif ch==10:    
        break
    else:
        print("Sorry wrong choice")