def find_max(left,right):
    if len(left)+len(right)<=2:
        return left+right
    else:
        total_len=len(left)+len(right)
        new_arr=left+right
        maximum=new_arr[0]
        idx=0
        main_val=new_arr[0]
        for i in range(1,total_len):
            if new_arr[i]**2>=maximum:
                maximum=new_arr[i]**2
                idx=i
                main_val=new_arr[i]
        sec_max=new_arr[0]
        for j in range(idx):
            if new_arr[j]>sec_max:
                sec_max=new_arr[j]
        return [sec_max,main_val]


def maximun_possibel(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_max=maximun_possibel(arr[:mid])
    right_max=maximun_possibel(arr[mid:])
    return find_max(left_max,right_max)
input_file=open('input2.txt','r')
output_file=open('output2.txt','w')
input_file.readline()
arr=[int(i) for i in input_file.readline().split()]
output=maximun_possibel(arr)
output_file.write(str(output[0]+output[1]**2))
