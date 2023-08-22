import math

def greedy_algo(tasks):

    completed_tasks = []
    last_end = -math.inf
    next_algo = []
    for task in tasks:
        if task[0] >= last_end:
            completed_tasks.append(task)
            last_end = task[1]
        else:
            next_algo.append(task)
    return completed_tasks, next_algo

input_file = open('input2_1.txt', 'r')
n, m = map(int, input_file.readline().split())
tasks = []
for _ in range(n):
    s, e = map(int, input_file.readline().split())
    tasks.append((s, e))
input_file.close()

count1 = 0
count2=0
tasks.sort(key=lambda x: x[0])
for _ in range(m):
    a, temp = greedy_algo(tasks)
    count1 += len(a)
    tasks = temp
tasks.sort(key=lambda x: x[1])
for _ in range(m):
    a, temp = greedy_algo(tasks)
    count2 += len(a)
    tasks = temp
# print(count1,count2)
output_file=open('output2_1.txt','w')
output_file.write(str(max(count1,count2)))
