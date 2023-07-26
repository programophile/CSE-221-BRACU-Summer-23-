from collections import defaultdict

class Vertex:
    def __init__(self, val):
        self.color = 0
        self.value = val

def colorin(G):
    for u in G.values():
        for i in u:
            i.color = 0

def DFS(G, u):
    u.color = 1
    for v in G[u.value]:
        if v.color == 0:
            if DFS(G, v):
                return True
        elif v.color == 1:
            return True
    u.color = 2
    return False

input_file = open('input4_1.txt', 'r')
n, m = map(int, input_file.readline().split())

vertices = [Vertex(i) for i in range(1, n+1)]
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input_file.readline().split())
    graph[u].append(vertices[v-1])

input_file.close()

colorin(graph)

output_file = open('output4_1.txt', 'w')

if DFS(graph, vertices[0]):
    output_file.write("YES")
else:
    output_file.write("NO")

output_file.close()
