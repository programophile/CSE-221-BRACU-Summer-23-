with open('input1a.txt') as file:
    n=int(file.readline())
    str1=""
    for i in range(n):
        a= file.readline().strip()
        # print(a)
        if int(a)%2==0:
            str1+=f"{a} is an even number\n"
        else:
            str1 += f"{a} is an odd number\n"
output=open('output1a.txt',"w")
output.write(str1)
output.close()