#implement binary search using array
class binary:
    def __init__(self):
        self.res=[]
        self.size=int(input("Enter the size of the array:"))
        print("Enter the items in ascending order")
        for i in range(self.size):
            self.val=int(input("Enter a item:"))
            self.res.append(self.val)
        self.item=int(input("Enter the search item:"))
    def display(self):
        print("List items are:",self.res)
        print("Search item is:",self.item)
    def search(self):
        lower=0
        upper=self.size-1
        while(lower<=upper):
            mid=(lower+upper)//2
            if self.item==self.res[mid]:
                return mid
                break
            elif self.item>=self.res[mid]:
                lower=mid+1
            else:
                upper=mid-1
        if(lower>upper):
            return -1
ob=binary()
ob.display()
r=ob.search()
if r==-1:
    print("Search item is invalid")
else:
    print("Position of search item is:",r)


#implement binary search using list
class binary:
    def __init__(self):
        print("Enter the items in ascending order")
        l1=input("Enter a list of items:").split()
        self.list=[int(i) for i in l1]
        self.item=int(input("Enter the search item:"))
        
    def display(self):
        print("List items are:",self.list)
        print("Search item is:",self.item)
        
    def search(self):
        lower=0
        upper=len(self.list)-1
        while(lower<=upper):
            mid=(lower+upper)//2
            if self.item==self.list[mid]:
                return mid
                break
            elif self.item>=self.list[mid]:
                lower=mid+1
            else:
                upper=mid-1
        if(lower>upper):
            return -1
ob=binary()
ob.display()
r=ob.search()
if r==-1:
    print("Search item is invalid")
else:
    print("Position of search item is:",r)
