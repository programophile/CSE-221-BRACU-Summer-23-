def sum_key(nk,arr1):
    n,key=map(int,nk.split())

    arr1=[int(i) for i in arr1.split()]
    str1=""
    for i in range(n):
        for j in range(i+1,n):
            if arr1[i]+arr1[j]==key:
                str1+=f'{i+1} {j+1}'
                output_file.write(str1)
                return
    str1+="Impossible"
    output_file.write(str1)

input_file=open("input1a.txt",'r')
output_file=open("output1a.txt",'w')
sum_key(input_file.readline(),input_file.readline())

