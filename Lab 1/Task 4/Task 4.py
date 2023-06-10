def train_sort(n):
    n=int(n)
    arr=[i.strip() for i in input_file.readlines()]
    str1=""
    for i in range(n):
        min_idx=i
        for j in range (i+1,n):
            if arr[min_idx].split()[0]>arr[j].split()[0]:
                min_idx=j
            elif arr[min_idx].split()[0]==arr[j].split()[0]:
                if arr[min_idx].split()[-1].split(":")[0]<arr[j].split()[-1].split(":")[0]:
                    min_idx=j
                elif arr[min_idx].split()[-1].split(":")[0]==arr[j].split()[-1].split(":")[0]:
                    if arr[min_idx].split()[-1].split(":")[1]<arr[j].split()[-1].split(":")[1]:
                        min_idx = j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]

    output_file.writelines([f"{line}\n" for line in arr])



input_file=open("input4.txt","r")
output_file=open("output4.txt",'w')

train_sort(input_file.readline())
input_file.close()
output_file.close()
