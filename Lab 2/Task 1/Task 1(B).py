def sum_algo(n,sum,arr1):
    temp=sum
    arr1=[int(i) for i in arr1.split()]
    dict1={}
    for i in range(n):
        if temp-arr1[i] in dict1:
            return i,dict1[temp-arr1[i]]
        else:
            dict1[arr1[i]]=i
    return "impssible"


print(sum_algo(int(input()),int(input()),input()))