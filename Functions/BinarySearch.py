arr = [1,2,3,4,5,6,7,8]
start=0
end=len(arr)-1


# Normal Loop
def binary(arr,start,end,target):
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid -1
    return -1            

print(binary(arr,start,end,4))

# using recursion
arr = [1,2,3,4,5,6,7,8]
start=0
end=len(arr)-1

def binary(arr,start,end,target):
    mid=(start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
            binary(arr,mid+1,end,target)
    else:
            binary(arr,start,mid-1,target)
    return -1            

print(binary(arr,start,end,4))    