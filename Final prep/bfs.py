from collections import defaultdict, deque
def bfs(graph,node):
    visited=set()
    queue=deque([node])
    visited.add(node)
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for u in graph[node]:
            if u not in visited:
                queue.append(u)
                visited.add(u)

n,m=map(int,input().split())
graph= defaultdict(list)
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
bfs(graph,1)