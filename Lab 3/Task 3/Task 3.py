def Partition(arr,low,high):
    pvt=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pvt:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def Quicksort(arr,p,r):
    if p<r:
        q=Partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)
arr=[9,5,4,6,1,3,2,9]
Quicksort(arr,0,len(arr)-1)
print(arr)