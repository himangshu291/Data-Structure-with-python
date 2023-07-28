def build_max_heap(arr):
    ind=(len(arr)//2)-1
    for i in range(ind,-1,-1):
        heapify(arr,i)
           
def heapify(a,i):
    l=2*i+1
    r=2*i+2
    lar=i
    if l<len(a) and a[l]>a[lar]:
        lar=l
    if r<len(a) and a[r]>a[lar]:
        lar=r
    if lar!=i:
        a[lar],a[i]=a[i],a[lar]
        heapify(a,lar)
arr=[90,85,30,60,86,100,40,54,69,35,95,80]
print(arr)
build_max_heap(arr)
print(arr)
  