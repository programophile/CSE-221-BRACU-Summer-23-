def find_max(arr):
    if len(arr)<=1:
        return arr[0]
    mid=len(arr)//2
    left_max=find_max(arr[:mid])
    right_max=find_max(arr[mid:])
    return max(left_max,right_max)
input_file=open('input4.txt','r')
output_file=open('output4.txt','w')
input_file.readline()
arr=input_file.readline()
arr=[int(i) for i in arr.split()]
max_num=find_max(arr)
output_file.write(str(max_num))