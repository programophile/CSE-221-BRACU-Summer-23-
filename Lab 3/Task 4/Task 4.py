def Partition(arr,k):
    if len(arr)==1:
        return arr[0]
    pvt=arr[-1]
    left_arr=[i for i in arr if i<pvt]
    right_arr=[i for i in arr if i>pvt]
    if len(left_arr)>=k:
        return Partition(left_arr,k)
    elif k > len(arr) - len(right_arr):
        return Partition(right_arr, k - len(arr) + len(right_arr))
    else:
        return pvt
input_file=open('input4.txt','r')
output_file=open('output4.txt','w')
n=input_file.readline()
arr=[int(i) for i in input_file.readline().split()]
str1=""
test_case=int(input_file.readline().split()[0])
for i in range(test_case):
    str1+=str(Partition(arr,int(input_file.readline())))+"\n"
output_file.write(str1)
