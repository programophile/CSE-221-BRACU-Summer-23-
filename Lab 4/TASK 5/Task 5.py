
from collections import defaultdict

class Vertex:
    def __init__(self, val):
        self.colour = 0
        self.value = val
        self.distance=0
        self.parent=None

def BFS(G, s,d):
    for u in G.values():
        for i in u:
         i.colour = 0

    Queue = []
    s.colour = 1
    Queue.append(s)

    while len(Queue) != 0:
        u = Queue.pop(0)
        if u.value==d:
            path=[u.value]
            parent=u.parent
            while parent!=None:
                path.append(parent.value)
                parent=parent.parent

            return u.distance,path[::-1]

        for v in G[u.value]:
            if v.colour == 0:
                v.colour = 1
                v.distance=u.distance+1
                v.parent=u
                Queue.append(v)
input_file=open('input5_1.txt','r')
n, m,d = map(int, input_file.readline().split())

vertices = [Vertex(i) for i in range(1, n+1)]
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input_file.readline().split())
    graph[u].append(vertices[v-1])  # Subtract 1 as the list is 0-indexed
    graph[v].append(vertices[u-1])  # Subtract 1 as the list is 0-indexed

a,b=BFS(graph, vertices[0],d)  # Start BFS from the first vertex (Vertex 1)
str1=""
str1+=f"Time:{a}\nShortest path:"
for i in b:
    str1+=str(i)+" "
output_file=open('output5_1.txt','w')
output_file.write(str1)