def sum_key(n):
    key=int(input())
    arr1=[int(i) for i in input().split()]
    for i in range(n):
        for j in range(i+1,n):
            if arr1[i]+arr1[j]==key:
                return i,j
    return "Impossible"
print(str(sum_key(int(input()))))