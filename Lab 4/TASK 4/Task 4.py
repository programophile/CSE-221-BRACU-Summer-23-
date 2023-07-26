from collections import defaultdict
class Vertex:
    def __init__(self, val):
        self.color = 0
        self.value = val
def colorin(G):
    for u in G.values():
        for i in u:
            i.color=0
def DFS(G,u):
    u.color=1
    for v in G[u.value]:
        if v.color==0:

            return DFS(G,v)
        elif v.color==1:
            # print("YES")

            return True
input_file=open('input4_1.txt','r')
n,m=map(int, input_file.readline().split())

vertices = [Vertex(i) for i in range(1, n+1)]
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input_file.readline().split())
    graph[u].append(vertices[v-1])  # Subtract 1 as the list is 0-indexed
    # graph[v].append(vertices[u-1])  # Su
colorin(graph)
output_file=open('output4_1.txt','w')

if DFS(graph,vertices[0])==True:
    output_file.write("YES")
else:
    output_file.write("NO")