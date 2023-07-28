#For max heap
def build_max_heap(arr):
    ind=(len(arr)//2)-1
    for i in range(ind,-1,-1):
        heapify_for_max_heap(arr,i,len(arr))
        
def heapsort_for_max_heap(a):
    build_max_heap(a)
    l=len(a)
    for i in range(l-1,0,-1):  
        a[i],a[0]=a[0],a[i]
        heapify_for_max_heap(a,0,i)

def heapify_for_max_heap(a,i,size):
    l=2*i+1
    r=2*i+2
    lar=i
    if l<size and a[l]>a[lar]:
        lar=l
    if r<size and a[r]>a[lar]:
        lar=r
    if lar!=i:
        a[lar],a[i]=a[i],a[lar]
        heapify_for_max_heap(a,lar,size)

#For min heap
 
def build_min_heap(arr):
    ind=(len(arr)//2)-1
    for i in range(ind,-1,-1):
        heapify_for_min_heap(arr,i,len(arr))
           
def heapsort_for_min_heap(a):
    build_min_heap(a)
    l=len(a)
    for i in range(l-1,0,-1):  
        a[i],a[0]=a[0],a[i]
        heapify_for_min_heap(a,0,i)
               
def heapify_for_min_heap(a,i,size):
    l=2*i+1
    r=2*i+2
    min=i
    if l<size and a[l]<a[min]:
        min=l
    if r<size and a[r]<a[min]:
        min=r
    if min!=i:
        a[min],a[i]=a[i],a[min]
        heapify_for_min_heap(a,min,size)
        

arr=[90,85,30,60,86,100,40,54,69,35,95,80]
print(arr)
# heapsort_for_min_heap(arr)
heapsort_for_max_heap(arr)
print(arr)
  
  
  
 
 
