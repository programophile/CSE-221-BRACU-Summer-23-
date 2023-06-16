def merge(a, b):
    merged_arr=[0]*(len(a)+len(b))
    temp1=0
    temp2=0
    merged_arr_indx=0
    while temp1<len(a) and temp2<len(b):
        if a[temp1]<b[temp2]:
            merged_arr[merged_arr_indx]=a[temp1]
            temp1+=1
        else:
            merged_arr[merged_arr_indx]=b[temp2]
            temp2+=1
        merged_arr_indx+=1
    while temp1<len(a):
        merged_arr[merged_arr_indx] = a[temp1]
        temp1 += 1
        merged_arr_indx += 1
    while temp2<len(b):
        merged_arr[merged_arr_indx] = b[temp2]
        temp2 += 1
        merged_arr_indx += 1
    return merged_arr
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)
print(mergeSort([2,1,4,5,7,2,9,9,1000,739,5,6,7,2,1,0,3]))