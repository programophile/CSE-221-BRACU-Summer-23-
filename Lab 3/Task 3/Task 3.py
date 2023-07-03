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

input_file=open('input3.txt','r')
output_file=open('output3.txt','w')
n=int(input_file.readline())
arr=[int(i) for i in input_file.readline().split()]
output=Quicksort(arr,0,n-1)
str1=""
for i in arr:
    str1+=str(i)+" "
output_file.write(str1)