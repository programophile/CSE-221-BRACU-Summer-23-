with open ("input1b.txt") as f:
    n=int(f.readline())
    str1=""
    for i in range(n):
        a=f.readline().strip("calculate").strip()
        str1+=f"The result of {a} is {eval(a)}\n"

output=open("output1b","w")
output.write(str1)
output.close()