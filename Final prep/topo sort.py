from collections import defaultdict,deque
def dfs_topo(graph):
    visited=set()
    result=[]

    def dfs(n):

        visited.add(n)
        for v in graph[n]:
            if v not in visited:
                dfs(v)
            elif v not in visited and v not in result:
                return []
        result.append(n)
    g=graph.copy()
    for k in g:
        if k not in visited:

            dfs(k)
    print(result[::-1])

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
        u = queue.popleft()
        output_arr.append(u)
        for v in graph[u]:
            in_degree_count[v] -= 1
            if in_degree_count[v] == 0:
                queue.append(v)

    return output_arr


n,m=map(int,input().split())
graph= defaultdict(list)
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    # graph[v].append(u)
visited=[]
dfs_topo(graph)
topological_sort_bfs(graph)