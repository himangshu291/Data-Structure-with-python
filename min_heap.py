def build_min_heap(arr):
    ind=(len(arr)//2)-1
    for i in range(ind,-1,-1):
        heapify(arr,i)
           
def heapify(a,i):
    l=2*i+1
    r=2*i+2
    min=i
    if l<len(a) and a[l]<a[min]:
        min=l
    if r<len(a) and a[r]<a[min]:
        min=r
    if min!=i:
        a[min],a[i]=a[i],a[min]
        heapify(a,min)
arr=[90,85,30,60,86,100,40,54,69,35,95,80]
print(arr)
build_min_heap(arr)
print(arr)
  