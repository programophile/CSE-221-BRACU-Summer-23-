from collections import defaultdict

def topological_sort_dfs(graph):
    def dfs(u):
        visited_node.add(u)
        for v in graph[u]:
            if v not in visited_node:
                dfs(v)
        result.append(u)
    visited_node = set()
    result = []


    copy_dict=graph.copy()
    for u in copy_dict.keys():
        if u not in visited_node:
            dfs(u)

    return result[::-1]
input_file=open('input1a_1.txt','r')
n,m=map(int, input_file.readline().split())
graph = defaultdict(list)
str1=""


for _ in range(m):
    u, v =map(int, input_file.readline().split())
    graph[u].append(v)

sorted_order = topological_sort_dfs(graph)
output_file=open('output1a_1.txt','w')
if len(sorted_order)!=n:
    str1="Impossible"
else:
    for i in sorted_order:
        str1+=str(i)+" "
output_file.write(str1)
print(sorted_order)
output_file.close()