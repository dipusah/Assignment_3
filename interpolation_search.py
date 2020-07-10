def interpolation_search(arr,n,key):
    s=0
    e=n-1
    while(s<=e and key>=arr[s] and key<=arr[e]):
        position=s+(((e-s)//(arr[e]-arr[s]))*(key-arr[s]))
        if arr[position]==key:
            return position
        elif key>arr[position]:
            s=position+1
        else:
            e=position-1
    return -1
arr=[1,4,5,6,7,8,9]
n=len(arr)
key=int(input('data from list:-'))
result=interpolation_search(arr,n,key)
if result!=-1:
    print('element is found at index %d'%result)
else:
    print("element is not found in the list.")