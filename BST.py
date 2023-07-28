class node:
    def __init__(self,value):
        self.key=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def createbst(self,lst):
        for item in lst:
            n=node(item)
            if self.root == None:
                self.root=n
            else:
                p=self.root
                # par=None
                while(p!=None):
                    if item<p.key:
                        par=p        #parent
                        p=p.left
                    else:
                        par=p
                        p=p.right
                if item<par.key:
                    par.left=n
                else:
                    par.right=n
    def search(self,item):
        # if self.root==None:
        #     return None
        p=self.root
        prev=None
        while(p!=None):
            if p.key==item:
                # print(p.key)
                # return p.key
                return prev,p    #prev=parent node address
            else:
                if item<p.key:
                    prev=p
                    p=p.left
                else:
                    prev=p
                    p=p.right
        print("Item not found") 
    def preorder(self,T):
        if T!=None:
            print(T.key,end=" ")
            self.preorder(T.left)
            self.preorder(T.right)
    def inorder(self,T): 
        if T!=None:
            self.inorder(T.left)
            print(T.key,end=" ")
            self.inorder(T.right)
    def postorder(self,T):
        if T!=None:
            self.postorder(T.left)
            self.postorder(T.right)
            print(T.key,end=" ")
    def height(self,T):
        if T==None:
            return 0
        else:
            return max(self.height(T.left),self.height(T.right))+1
    def delete(self,t):
        par,value= self.search(t)           #par is parent node and value is search  item node
        p= value
        parent=par
        while p!=None:
            if value.left==None and value.right==None:
                print("No child")
                parent.left=None
                parent.right=None
                del value
                # print(value)
                return
            elif value.left==None and value.right!=None:
                print("One child")
                child=value.right
                print("child is:",child.key)
                if parent.key>child.key:
                    parent.left=child
                else:
                    parent.right=child
                print("Parent key is:",parent.key)
                del value
                # print(value)
                return
            elif value.left!=None and value.right==None:
                print("One child")
                child=value.left
                print("child is:",child.key)
                if parent.key>=child.key:
                    parent.left=child
                else:
                    parent.right=child
                print("Parent key is:",parent.key)
                del value
                # print(value)
                return
            else:
                print("Two child")
                parinsucc=value
                insucc=value.right
                while insucc.left!=None:
                    parinsucc=insucc
                    insucc=insucc.left
                print("Inorder successor:",insucc.key)
                key1=insucc.key
                if parinsucc.left==insucc:
                    parinsucc.left=None
                else:
                    parinsucc.right=None
                value.key=key1
                del key1
                # print(value)
                return
        print("Item is not found.")
        
        
val=[100,50,90,130,110,150,120,30,20,45,130,140,115,105]
ob=BST()
# list=input("Enter a list of values:").split()
# val=[int(i) for i in list]
root=ob.createbst(val)
print("Preorder traversal:",end=" ")
ob.preorder(ob.root)
print("\nInorder traversal:",end=" ")
ob.inorder(ob.root)
print("\nPostorder traversal:",end=" ")
ob.postorder(ob.root)
res=ob.height(ob.root)
print("\nHeight of the tree:",res)
item=int(input("\nEnter the search item:"))
r=ob.search(item)
# if r==-1:
#     print("Item not found")             
# else:
#     print("Item found")
print("parent node of search item is:",r)
ob.delete(int(input("Enter the deleted item:")))
print("\nInorder traversal:",end=" ")
ob.inorder(ob.root)