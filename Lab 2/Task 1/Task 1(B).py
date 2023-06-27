def sum_algo(n,sum,arr1):
    temp=sum
    arr1=[int(i) for i in arr1.split()]
    dict1={}
    str1=""
    for i in range(n):
        if temp-arr1[i] in dict1:
            str1+=f"{dict1[temp-arr1[i]]+1} {i+1}"
            output_file.write(str1)
            return
        else:
            dict1[arr1[i]]=i
    str1+="Impossible"
    output_file.write(str1)


input_file=open("input1b.txt",'r')
n,sum=map(int,input_file.readline().split())
output_file=open("output1b.txt",'w')
sum_algo(n,sum,input_file.readline())
