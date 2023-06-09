
def selection_sort(n):
    str1=""
    n=int(n)
    arr_id=[int(i) for i in input_file.readline().split()]
    arr_mark=[int(i) for i in input_file.readline().split()]
    for i in range(n):
        max_idx=i
        for j in range(i+1,n):
            if arr_mark[j]==arr_mark[i] and arr_id[j]<arr_id[max_idx]:
                max_idx = j
            elif arr_mark[j]>arr_mark[max_idx]:
                max_idx=j

        arr_mark[i],arr_mark[max_idx]=arr_mark[max_idx],arr_mark[i]
        arr_id[i],arr_id[max_idx]=arr_id[max_idx],arr_id[i]
    for i in range(n):
        str1+=f"ID: {arr_id[i]} Mark: {arr_mark[i]}\n"
    output_file=open("output3.txt",'w')
    output_file.write(str1)
    output_file.close()
input_file=open("input3.txt","r")
selection_sort(input_file.readline())
input_file.close()