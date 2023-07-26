
from collections import defaultdict

class Vertex:
    def __init__(self, val):
        self.colour = 0
        self.value = val

def BFS(G, s):
    str1=""
    for u in G.values():
        for i in u:
         i.colour = 0

    Queue = []
    s.colour = 1
    Queue.append(s)

    while len(Queue) != 0:
        u = Queue.pop(0)
        str1+=str(u.value)+" "

        for v in G[u.value]:
            if v.colour == 0:
                v.colour = 1
                Queue.append(v)
    return str1
input_file=open('input2_1.txt','r')
n,m=map(int,input_file.readline().split())

vertices = [Vertex(i) for i in range(1, n+1)]
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input_file.readline().split())
    graph[u].append(vertices[v-1])
    graph[v].append(vertices[u-1])
output_file=open('output2_1.txt','w')
output_file.write(BFS(graph, vertices[0]))
output_file.close()

