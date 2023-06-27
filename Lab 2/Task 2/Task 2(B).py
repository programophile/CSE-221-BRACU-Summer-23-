def merge(n1,arr1,n2,arr2):
    arr1=[int(i) for i in arr1.split()]
    arr2=[int(i) for i in arr2.split()]
    n1=int(n1)
    n2=int(n2)
    new_arr=[None]*(n1+n2)
    temp=0
    temp2=0
    count=0
    while temp!=n1 and temp2!=n2 :
        if arr1[temp]<arr2[temp2]:
            new_arr[count]=arr1[temp]
            temp+=1
            count+=1
        else:
            new_arr[count]=arr2[temp2]
            temp2+=1
            count+=1
    while temp<n1:
        new_arr[count]=arr1[temp]
        count+=1
        temp+=1
    while temp2<n2:
        new_arr[count]=arr2[temp2]
        count+=1
        temp2+=1
    return new_arr

input_file=open("input2b.txt",'r')
output_file=open('output2b.txt','w')
output_arr=merge(input_file.readline(),input_file.readline(),input_file.readline(),input_file.readline())
str1=""
for i in output_arr:
    str1+=f"{str(i)} "
output_file.write(str1)