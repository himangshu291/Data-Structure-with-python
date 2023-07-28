class sort:
    def __init__(self):
        self.res=[]
        self.size=int(input("Enter the size of the array:"))
        for i in range(self.size):
            self.item=int(input("Enter a item:"))
            self.res.append(self.item)
        print("Before Sorting:")
        print(self.res)
        
    #BUBBLE SORT 
    def bubble_sort(self):
        for i in range(1,self.size):              # Loop to select no. of iteration
            for j in range(0,(self.size-i)):        # loop to compare elements of every iteration
                if self.res[j]>self.res[j+1]:       # compare 1st no. with 2nd number
                    (self.res[j],self.res[j+1])=(self.res[j+1],self.res[j])
        print("After bubble Sort:")
        print(self.res)
    
    #SELECTION SORT IN ASCENDING ORDER 
    def selection_sort_asc(self):
        for i in range(1,self.size):
            min=i-1
            for j in range(i,self.size):
                if self.res[j]<self.res[min]:
                    min=j
            (self.res[i-1],self.res[min])=(self.res[min],self.res[i-1])
        print("After selection sort in ascending order:")
        print(self.res)
            
    #SELECTION SORT IN DESCENDING ORDER   
    def selection_sort_desc(self):
        for i in range(1,self.size):
            max=i-1
            for j in range(i,self.size):
                if self.res[max]<self.res[j]:
                    max=j
            (self.res[i-1],self.res[max])=(self.res[max],self.res[i-1])
        print("After selection sort in descending order:")
        print(self.res)
        
    #INSERTION SORT
    def insertion_sort(self):
        for i in range(1,self.size):                # Loop to select no. of iteration
            tmp=self.res[i]                        
            j=i-1
            while(tmp<self.res[j] and j>=0):        # loop to compare elements of every iteration
                self.res[j+1]=self.res[j]
                j-=1
            self.res[j+1]=tmp                       #tmp stored in its proper place
        print("After insertion Sort:")
        print(self.res)
        
ob=sort()
ob.bubble_sort()
ob.selection_sort_asc()
ob.selection_sort_desc()
ob.insertion_sort()