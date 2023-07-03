def merge(a, b,count):
    merged_arr=[0]*(len(a)+len(b))
    temp1=0
    temp2=0
    merged_arr_indx=0
    while temp1<len(a) and temp2<len(b):
        if a[temp1]<b[temp2]:
            merged_arr[merged_arr_indx]=a[temp1]
            temp1+=1
            # count+=1
        else:
            merged_arr[merged_arr_indx]=b[temp2]
            # print(b[temp2])
            temp2+=1
            count+=len(a)-temp1


        merged_arr_indx+=1
    while temp1<len(a):
        merged_arr[merged_arr_indx] = a[temp1]
        temp1 += 1
        merged_arr_indx += 1
    while temp2<len(b):
        merged_arr[merged_arr_indx] = b[temp2]
        temp2 += 1
        merged_arr_indx += 1
    return [merged_arr,count]


def count_allian(arr,count):
    count=0
    if len(arr) <= 1:
        return [arr,0]
    else:
        mid = len(arr)//2
        left = count_allian(arr[:mid],count)
        count+=left[1]
        right= count_allian(arr[mid:],count)
        count+=right[1]
        a=merge(left[0], right[0],count)
        count+=a[1]
        return a
input_file=open('input1.txt','r')
output_file=open('output1.txt','w')
input_file.readline()
arr=[int(i) for i in input_file.readline().split()]
output=count_allian(arr,0)
output_file.write(str(output))