def binarysearch(arr, target):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=start+end//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1
arr=list(map(int,input().split()))
target=int(input())
s=binarysearch(arr,target)
if s==-1:
    print("No element found")
else:
    print("Element Found")


    