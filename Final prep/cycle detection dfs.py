from collections import defaultdict


def dfs(graph, node, visited):
    visited[node] = 1
    print(node)
    for v in graph[node]:
        if visited[v]==0:
             dfs(graph, v, visited)
                # return True
        elif visited[v]==1:
            print("YES")

            # return True
    visited[node]=2
    # print(visited)
    # return False


n, m = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    # graph[v].append(u)
visited = dict()
for i in range(1,n+1):
    visited[i]=0
print(dfs(graph, 1, visited))

