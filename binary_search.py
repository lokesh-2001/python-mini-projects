#iterative
def binary_search(list1,n):
    low=0
    high=len(list1)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if(list1[mid]<n):
            low=mid+1
        elif(list1[mid]>n):
            high=mid-1
        else:
            return mid

"""#recursive
def binary_search(list1,low,high,n):
    if(low<=high):
        mid=(low+high)//2
        if(list1[mid]==n):
            return mid
        elif(list1[mid]>n):
            return binary_search(list1,low,mid-1,n)
        else:
            return binary_search(list1,mid+1,high,n)
            
    else:
        return -1
"""


ls=[12,32,36,45,56,78,89]
n=32

#res=binary_search(ls,0,len(ls)-1,n)
res=binary_search(ls,n)

if(res!=-1):
    print("Element present at index: "+str(res))
else:
    print("element not found!!")