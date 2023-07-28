class node:
    def __init__(self,co,exp):
        self.coef=co
        self.exp=exp
        self.link=None
class Polylinked:
    def __init__(self):
        self.start=None
    def add(self,co,e):
        if self.start==None:
            n=node(co,e)
            self.start=n
            return
        else:
            prev=None
            p=self.start
            while(p!=None and p.exp!=e):
                prev=p
                p=p.link
            if p!=None:
                p.coef+=co
                return
            else:
                p1=self.start
                prev=None
                while p1!=None and p1.exp>e:
                    prev=p1
                    p1=p1.link
                if p1 == None:
                    pnew=node(co,e)
                    prev.link=pnew
                else:
                    pnew=node(co,e)
                    if prev == None:
                        pnew.link=self.start
                        self.start=pnew
                    else:
                        pnew.link=p1
                        prev.link=pnew
    def display(self):
        if self.start==None:
            print("Empty Linked List")
            return
        else:
            p=self.start
            # print("Nodes of singly linked list:")
            while(p!=None):
                print("(",p.coef,"x^",p.exp,")",end=" ")
                p=p.link
ob=Polylinked()
# while(True):
#     print("--------------------------")
#     print("\n******MENU******")
#     print("1. Add_node 2.Display 3.Exit)
          
ob.add(6,7)
ob.add(3,4)
ob.add(3,5)
ob.add(7,8)
ob.display()
    