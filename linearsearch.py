#implement linear search using list
class linear:
    def __init__(self):
        l1=input("Enter a list of items:").split()
        self.list=[int(i) for i in l1]
        self.item=int(input("Enter the search item:"))
    def display(self):
        print("List items are:",self.list)
        print("Search item is:",self.item)
    def search(self):
        i=0
        while(i<len(self.list)):
            if self.item==self.list[i]:
                return i
                break
            i+=1
        if(i==len(self.list)):
            return -1
ob=linear()
ob.display()
res=ob.search()
if res==-1:
    print("Search item is invalid")
else:
    print("Position of search item is:",res)
    
#implement linear search using array
class linear:
    def __init__(self):
        self.res=[]
        self.size=int(input("Enter the size of the array:"))
        for i in range(self.size):
            self.val=int(input("Enter a item:"))
            self.res.append(self.val)
        self.item=int(input("Enter the search item:"))
    def display(self):
        print("List items are:",self.res)
        print("Search item is:",self.item)
    def search(self):
        i=0
        while(i<self.size):
            if self.item==self.res[i]:
                return i
                break
            i+=1
        if(i==self.size):
            return -1
ob=linear()
ob.display()
r=ob.search()
if r==-1:
    print("Search item is invalid")
else:
    print("Position of search item is:",r)

