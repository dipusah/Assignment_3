def binary_search(arr,n,data):
    l=0
    r=n-1
    mid=0
    while(l<r):
        mid=(l+r)//2
        if data==arr[mid]:
            return mid
        elif(data < arr[mid]):
            r=r-1
        else:
            l=mid+1
    return -1
arr=[1,4,5,6,7,8,9]
n=len(arr)
data=int(input('data from list:-'))
result=binary_search(arr,n,data)
if result!=-1:
    print('element is found at index %d'%result)
else:
    print("element is not found in the list.")


