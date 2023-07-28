class node:
    def __init__(self,value):
        self.prev=None
        self.info=value
        self.link=None   
class dclinked:
    def __init__(self):
        self.start=None
    # def insert_at_beginning(self,value):
    #     n=node(value)
    #     if self.start==None:
    #         self.start=n
    #     elif(self.start.prev==None):
    #         p=self.start
    #         n.link=p
    #         p.prev=n
    #         p.link=n
    #         n.prev=p
    #     else:
    #         p=self.start
    #         v=self.start.prev
    #         n.link=p
    #         self.start=n
    #         self.start.prev=v
    #         v.link=self.start
    #         p.prev=n
    #         # print(self.start.info)
    #         q=self.start.prev
    #         print(q.info)
        
            
    # def insert_at_end(self,value):
    #     n=node(value)
    #     if self.start==None:
    #         self.start=n
    #     else:
    #         p=self.start
    #         while p.link!=None:
    #             p=p.link
    #         p.link=n
    #         n.prev=p
            
    # def insert_at_specified_position(self,pos,value):
    #     n=node(value)
    #     if self.start==None:
    #         self.start=n
    #     elif(pos==1):
    #         self.insert_at_beginning(value)
    #         return
    #     else:
    #         i=1
    #         p=self.start
    #         while i<pos-1:
    #             if p!=None:
    #                 p=p.link
    #                 i+=1
    #             else:
    #                 print("Invalid position")
    #                 return
    #         t=p.link
    #         n.link=t
    #         p.link=n
    #         n.prev=p
            
    # def insert_after_specified_item(self,item,value):
    #     n=node(value)
    #     if self.start==None:
    #         self.start=n
    #     elif self.start.info==value:
    #         self.insert_at_beginning(value)
    #     else:
    #         p=self.start
    #         while p!=None or p.info!=item :
    #             p=p.link
    #         if p==None:
    #             print("Item invalid")
    #             return
    #         n.link=p.link
    #         p.link=n
                   
    # def delete_start_node(self):
    #     if self.start==None:
    #         print("Empty Linked List")
    #         return 0
    #     else:
    #         p=self.start
    #         item=p.info
    #         self.start=p.link
    #         self.start.prev=None
    #         del p
    #         return item
        
    # def delete_last_node(self):
    #     if self.start==None:
    #         print("Empty Linked List")
    #         return 0
    #     elif(self.start.link==None):
    #         p=self.start
    #         self.start=None
    #         item=p.info
    #         del p
    #         return item
    #     else:
    #         p=self.start
    #         while p.link!=None:
    #             p=p.link
    #         item=p.info
    #         q=p.prev
    #         q.link=None
    #         del p
    #         return item
        
    # def delete_at_specified_pos_node(self,pos):
    #     if self.start==None:
    #         print("Empty Linked List")
    #         return 0
    #     elif(pos==1):
    #         self.delete_start_node()
    #         return
    #     else:
    #         i=1
    #         p=self.start
    #         while i<pos-1:
    #             if p.link!=None:
    #                 prev=p
    #                 p=p.link
    #                 i+=1
    #             else:
    #                 print("Invalid position")
    #                 return
    #         q=p.link
    #         item=q.info
    #         t=p.link.link
    #         p.link=t
    #         t.prev=p
    #         del p
    #         return item
    
    # def delete_node_after_specified_item(self,item):
    #     if self.start==None:
    #         print("Empty Linked List")
    #     if self.start.info==value:
    #         self.delete_start_node()
    #         return
    #     p=self.start
    #     while p!=None and p.info!=item:
    #         prev=p
    #         p=p.link
    #     if p==None:
    #         print("Given item doesn't exist in the linked list")
    #         return
    #     prev.link=p.link
    #     p.link=None
    #     del p
        
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
    # def search(self,item):
    #     p=self.start
    #     c=0
    #     while(p!=None):
    #         if(p.info==item):
    #             p=p.link
    #             c+=1
    #         else:
    #             p=p.link
    #     if c==1:
    #         print("Item found")
    #     else:
    #         print("Item not found")
    
ob=dclinked()
while(True):
    print("--------------------------")
    print("\n******MENU******")
    print(" 1.insert_at_beginning \n 2.insert_at_end \n 3.insert_at_specified_position \n 4.insert_after_specified_item \n 5.delete_start_node \n 6.delete_last_node \n 7.delete_at_specified_pos_node \n 8.delete_node_after_specified_item \n 9.Display \n 10.Search \n 11.EXIT")
    ch=int(input("Enter your choice:"))        
    if ch==1:
        ob.insert_at_beginning(int(input("\nEnter the value:")))
    # elif ch==2:
    #     ob.insert_at_end(int(input("\nEnter the value:")))
    # elif ch==3:
    #     pos=int(input("\nEnter the position:"))
    #     value=int(input("\nEnter the value:"))
    #     ob.insert_at_specified_position(pos,value)
    # # elif ch==4:
    # #     item=int(input("\nEnter the item:"))
    # #     value=int(input("\nEnter the value:"))
    # #     ob.insert_after_specified_item(item,value)
    # elif ch==5:
    #     res=ob.delete_start_node()
    #     if res!=0:
    #         print("Item deleted")
    #         print("Deleted item:",res)
    # elif ch==6:
    #     res=ob.delete_last_node() 
    #     if res!=0:
    #         print("Item deleted")
    #         print("Deleted item:",res)
    # elif ch==7:
    #     res=ob.delete_at_specified_pos_node(int(input("\nEnter the position:")))
    #     if res!=0:
    #         print("Item deleted")
    #         print("Deleted item:",res)
    # elif ch==8:
    #     ob.delete_node_after_specified_item(int(input+*9/8("\nEnter the item:")))
    elif ch==9:
        ob.display()
    # elif ch==10:
    #     ob.search(int(input("Enter the search item:")))
    elif ch==11:    
        break
    else:
        print("Sorry wrong choice")