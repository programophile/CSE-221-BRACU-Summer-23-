#1
import math
def greddy_algo(n,tasks):
    tasks.sort(key=lambda x: x[1])
    completed_tasks = []
    last_end = -math.inf
    for task in tasks:
        if task[0] >= last_end:
            completed_tasks.append(task)
            last_end = task[1]
    return completed_tasks
input_file=open('input1_1.txt','r')
n=int(input_file.readline())
tasks=[]
for _ in range(n):
    s,e=map(int,input_file.readline().split())
    tasks.append((s,e))
a=greddy_algo(n,tasks)
str1=""

output_file=open('output1_1.txt','w')
str1+=str(len(a))
for i in a:
    str1+=f"\n{i[0]} {i[1]}"
output_file.write(str1)
output_file.close()

