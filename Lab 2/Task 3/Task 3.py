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
input_file=open('input3.txt','r')
output_file=open('output3.txt','w')
input_file.readline()
arr=input_file.readline()
arr=[int(i) for i in arr.split()]
sorted_arr=mergeSort(arr)
str1=""
for i in sorted_arr:
    str1+=f"{str(i)} "
output_file.write(str1)