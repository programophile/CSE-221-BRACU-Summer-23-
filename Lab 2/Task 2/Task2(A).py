def merge(n1,arr1,n2,arr2):
    arr1=[int(i) for i in arr1.split()]
    arr2=[int(i) for i in arr2.split()]
    arr1.extend(arr2)
    arr1.sort()
    return arr1
input_file=open("input2a.txt",'r')
output_file=open('output2a.txt','w')
output_arr=merge(input_file.readline(),input_file.readline(),input_file.readline(),input_file.readline())
str1=""
for i in output_arr:
    str1+=f"{str(i)} "
output_file.write(str1)