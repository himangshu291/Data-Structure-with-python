class node:
    def __init__(self,value):
        self.key=value
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def create(self,lst):
        for item in lst:
            n=node(item)
            if self.root==None:
                self.root=n
            else:
                p=self.root
                while(p!=None):
                    if(item<p.key):
                        par=p
                        p=p.left
                    else:
                        par=p
                        p=p.right
                if item<par.key:
                    par.left=n
                else:
                    par.right=n
    def search(self,item):
        if self.root==None:
            print("Empty tree")
        else:
            p=self.root
            prev=None
            while(p!=None):
                if item==p.key:
                    print("Item found")
                    return
                elif(item<p.key):
                    prev=p
                    p=p.left
                else:
                    prev=p
                    p=p.right
            print("Item not found")
    def preorder(self,t):
        if t!=None:
            print(t.key,end=" ")
            self.preorder(t.left)
            self.preorder(t.right)
    def inorder(self,t):
        if t!=None:
            self.inorder(t.left)
            print(t.key,end=" ")
            self.inorder(t.right)
    def postorder(self,t):
        if t!=None:
            self.postorder(t.left)
            self.postorder(t.right)
            print(t.key,end=" ")
    def height(self,t):
        if t==None:
            return 0
        else:
            return max(self.height(t.left), self.height(t.right))+1   
    
val=[100,50,90,130,110,150,120,30,20,45,130,140,115,105]
ob=bst()
root=ob.create(val)
print("The preorder traversal is:",end=" ")
ob.preorder(ob.root)
print("\nThe inorder traversal is:",end=" ")
ob.inorder(ob.root)
print("\nThe postorder traversal is:",end=" ")
ob.postorder(ob.root)
height=ob.height(ob.root)
print("\nHeight of the tree is:",height)
ob.search(int(input("Enter the search item:")))