from collections import defaultdict
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        print(node, end=' ')

        for v in graph[node]:
            if v not in visited:
                dfs(graph, v, visited)


n,m=map(int,input().split())
graph= defaultdict(list)
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited=[]
dfs(graph,1,visited)

