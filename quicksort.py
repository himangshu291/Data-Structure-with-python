def quicksort(a,lb,ub):
    if lb<ub:
        piv=quick(a,lb,ub)
        quicksort(a,lb,piv-1)
        quicksort(a,piv+1,ub)
def quick(a,lb,ub):
    pivot=lb
    start=lb
    end=ub
    while(True):
        # Compare pivot with end
        # left search
        while(a[pivot]<=a[end]) and start<=end:
            end-=1
        if(start>end):
            return pivot        #Pivot in its proper place
        if(a[pivot]>a[end]):
            a[pivot],a[end]=a[end],a[pivot]
            pivot=end
            end-=1
            
        # Compare pivot with start
        # right search
        while(a[pivot]>=a[start]) and start<=end:
            start+=1
        if(start>end):
            return pivot        #Pivot in its proper place
        if(a[pivot]<a[start]):
            a[pivot],a[start]=a[start],a[pivot]
            pivot=start
            start+=1
        # if(start>end):
        #     return pivot        #Pivot in its proper place
l=input("Enter list of elements:").split()
lst=[int(i) for i in l]
quicksort(lst,0,len(lst)-1)
print(lst)

