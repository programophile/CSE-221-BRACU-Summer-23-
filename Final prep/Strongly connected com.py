from collections import defaultdict

def dfs(u, graph, visited, stack):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited, stack)
    stack.append(u)

def transpose_graph(graph):
    transposed = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transposed[v].append(u)
    return transposed

def find_strongly_connected_components(graph):
    visited = defaultdict(bool)
    stack = []
    copy_g=graph.copy()
    for u in copy_g:
        if not visited[u]:
            dfs(u, graph, visited, stack)

    transposed = transpose_graph(graph)
    visited = defaultdict(bool)
    components = []

    while stack:
        u = stack.pop()
        if not visited[u]:
            component = []
            dfs(u, transposed, visited, component)
            components.append(component)

    return components
n,m=map(int,input().split())
graph= defaultdict(list)
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)

visited=[]
print(find_strongly_connected_components(graph))