def binarysearch(arr, key):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            right=mid-1    
        else:
            left=mid+1
    return -1
arr=list(map(int,input().split()))
key=int(input())
r=binarysearch(arr, key)
if r==-1:
    print("element not round")
else:
    print("element found")
    