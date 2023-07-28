# def toh(n,source,auxiliary,destination):
#     if n==1:
#         print("Move disk 1 from source",source,"to destination",destination)
#         return 1
#     else:
#         count1=toh(n-1,source,destination,auxiliary)
#         print("Move disk",n,"from source",source,"to destination",destination)
#         count2=toh(n-1,auxiliary,source,destination)
#         return count1 + 1 + count2
# d=int(input("Enter the no. of disks:"))
# count=toh(d,'A','B','C')
# print("Number of Moves:",count)

# another method
def toh(n,source,auxiliary,destination):
    global count
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        count+=1
        return 
    else:
        toh(n-1,source,destination,auxiliary)
        count+=1
        print("Move disk",n,"from source",source,"to destination",destination)
        toh(n-1,auxiliary,source,destination)
d=int(input("Enter the no. of disks:"))
count=0
toh(d,'B','A','E')
print("Number of Moves:",count)
