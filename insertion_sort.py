def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        value=arr[i]
        hole=i
        while(hole>0 and arr[hole-1]>value):
            arr[hole],arr[hole-1]=arr[hole-1],arr[hole]
            hole=hole-1

        arr[hole]=value
arr=[4,5,2,3,8,6,9,7]
insertion_sort(arr)
for i in range(len(arr)):
    print("%d" %arr[i])