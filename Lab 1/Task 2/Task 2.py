def bubbleSort(arr):
    count=0
    arr=[int(i) for i in arr.split()]
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count+=1
        if count==0:
            # print("comN")
            output_file.write(str(arr))
            return arr
    output_file.write(str(arr))
    return arr
input_file=open("input2.txt","r")

# print(bubbleSort(input_file.readlines()[1:]))
input_file.readline()
output_file=open("output2.txt",'w')
bubbleSort(input_file.readline())
input_file.close()
output_file.close()