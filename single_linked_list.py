class node:
    def __init__(self,value):
        self.info=value
        self.link=None     
class slinked:
    def __init__(self):
        self.start=None
    def insert_at_beginning(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
        else:
            n.link=self.start
            self.start=n
        print("Item inserted at beginning")
            
    def insert_at_end(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
        else:
            p=self.start
            while p.link!=None:
                p=p.link
            p.link=n
        print("Item inserted at end")
            
    def insert_at_specified_position(self,pos,value):
        n=node(value)
        if self.start==None:
            self.start=n
        elif(pos==1):
            self.insert_at_beginning(value)
            return
        else:
            i=1
            p=self.start
            while i<pos:
                if p!=None:
                    prev=p
                    p=p.link
                    i+=1
                else:
                    print("Invalid position")
                    return
            n.link=p
            prev.link=n
        print("Item inserted at specified position")
            
    def insert_after_specified_item(self,item,value):
        n=node(value)
        if self.start==None:
            self.start=n
        elif self.start.info==value:
            self.insert_at_beginning(value)
        else:
            p=self.start
            while p!=None and p.info!=item :
                p=p.link
            if p==None:
                print("Item invalid")
                return
            n.link=p.link
            p.link=n
        print("Item inserted after specified item")
                   
    def delete_start_node(self):
        if self.start==None:
            print("Empty Linked List")
        else:
            p=self.start
            self.start=p.link
            item=p.info
            del p
            return item
        print("Starting node deleted")
        
    def delete_last_node(self):
        if self.start==None:
            print("Empty Linked List")
        else:
            p=self.start
            while p.link!=None:
                prev=p
                p=p.link
            item=p.info
            prev.link=None
            del p
            return item
        print("Last node deleted")
        
    def delete_at_specified_pos_node(self,pos):
        if self.start==None:
            print("Empty Linked List")
            return
        elif(pos==1):
            self.delete_start_node()
            return
        else:
            i=1
            p=self.start
            while i<pos:
                if p.link!=None:
                    prev=p
                    p=p.link
                    i+=1
                else:
                    print("Invalid position")
                    return
            item=p.info
            prev.link=p.link
            del p
            return item
        print("Specified position node deleted")
    
    def delete_specified_item_node(self,item):
        if self.start==None:
            print("Empty Linked List")
        if self.start.info==item:
            self.delete_start_node()
            return
        p=self.start
        while p!=None and p.info!=item:
            prev=p
            p=p.link
        if p==None:
            print("Given item doesn't exist in the linked list")
            return
        prev.link=p.link
        p.link=None
        del p
        print("Specified item node deleted")
        
    def display(self):
        if self.start==None:
            print("Empty Linked List")
            return
        else:
            p=self.start
            print("Nodes of singly linked list:")
            while(p!=None):
                print(p.info)
                p=p.link
    def search(self,item):
        p=self.start
        c=0
        while(p!=None):
            if(p.info==item):
                p=p.link
                c+=1
            else:
                p=p.link
        if c==1:
            print("Item found")
        else:
            print("Item not found")
    def reverse(self):
        c=None
        n=self.start
        if n==None:
            self.start=n
            return
        else:
            while n!= None:
                t=n.link
                n.link=c
                c=n
                n=t
            self.start=c
        

    
ob=slinked()
while(True):
    print("--------------------------")
    print("\n******MENU******")
    print(" 1.insert_at_beginning \n 2.insert_at_end \n 3.insert_at_specified_position \n 4.insert_after_specified_item \n 5.delete_start_node \n 6.delete_last_node \n 7.delete_at_specified_pos_node \n 8.delete_specified_item_node \n 9.Display \n 10.Search \n 11.Reverse \n 12.EXIT")
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
        ob.delete_specified_item_node(int(input("\nEnter the item:")))
    elif ch==9:
        ob.display()
    elif ch==10:
        ob.search(int(input("Enter the search item:")))
    elif ch==11:
        ob.reverse()
    elif ch==12:    
        break
    else:
        print("Sorry wrong choice")