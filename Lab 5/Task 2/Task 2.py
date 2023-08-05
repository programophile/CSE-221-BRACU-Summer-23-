from collections import defaultdict, deque


def topological_sort_bfs(graph):
    in_degree_count = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree_count[v] += 1
    queue=deque()
    for u in graph:
        if in_degree_count[u]==0:
            queue.append(u)

    output_arr = []


    while len(queue)!=0:
        queue=deque(sorted(queue))

        u = queue.popleft()
        output_arr.append(u)
        for v in graph[u]:
            in_degree_count[v] -= 1
            if in_degree_count[v] == 0:
                queue.append(v)

    return output_arr





input_file=open('input2_2.txt','r')
n,m=map(int, input_file.readline().split())
graph = defaultdict(list)
str1=""


for _ in range(m):
    u, v =map(int, input_file.readline().split())
    graph[u].append(v)

sorted_order = topological_sort_bfs(graph)
output_file=open('output2_2.txt','w')
if len(sorted_order)!=n:
    str1="Impossible"
else:
    for i in sorted_order:
        str1+=str(i)+" "
output_file.write(str1)
print(sorted_order)
output_file.close()