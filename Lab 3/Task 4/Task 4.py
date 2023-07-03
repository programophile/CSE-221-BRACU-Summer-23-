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

arr =[10, 11, 10, 6, 7, 9, 8, 15, 2]
print(Partition(arr, 5))
print(arr)
