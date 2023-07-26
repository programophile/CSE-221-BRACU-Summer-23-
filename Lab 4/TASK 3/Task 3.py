from collections import defaultdict
class Vertex:
    def __init__(self, val):
        self.color = 0
        self.value = val
def colorin(G):
    for u in G.values():
        for i in u:
            i.color=0
def DFS(G,u,str1):
    u.color=1
    str1 += str(u.value) + " "
    for v in G[u.value]:
        if v.color==0:

            str1=DFS(G,v,str1)
    return str1
input_file=open('input3_1.txt','r')
n,m=map(int, input_file.readline().split())
vertices = [Vertex(i) for i in range(1, n+1)]
graph = defaultdict(list)
str1=""

for _ in range(m):
    u, v =map(int, input_file.readline().split())
    graph[u].append(vertices[v-1])  # Subtract 1 as the list is 0-indexed
    graph[v].append(vertices[u-1])  # Su
colorin(graph)
a=DFS(graph,vertices[0],str1)
output_file=open('output3_1.txt','w')
output_file.write(a)