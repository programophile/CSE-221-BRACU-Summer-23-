def dijkstra(graph, start):
    distance_node = {x: float('inf') for x in graph}

    distance_node[start] = 0
    visited = set()
    while len(visited) < len(graph):
        min_distance = float('inf')
        curr_node = None

        for node in graph:
            if node not in visited and distance_node[node] < min_distance:
                curr_node = node
                min_distance = distance_node[node]
        if curr_node==None:
            return distance_node
        visited.add(curr_node)

        for neighbor, weight in graph[curr_node].items():
            distance = distance_node[curr_node] + weight
            if distance < distance_node[neighbor]:
                distance_node[neighbor] = distance
    return distance_node

input_file=open('input1_1.txt','r')
n,m=map(int, input_file.readline().split())
# print(n,m)
graph = {i: {} for i in range(1, n+1)}

for _ in range(m):
    u,v,w=map(int, input_file.readline().split())
    graph[u][v] = w
start = int(input_file.readline())

distances = dijkstra(graph, start)
str1=""

for i in range(1, n+1):
    if distances[i] == float('inf'):
        str1+="-1 "
    else:
        str1+=f"{distances[i]} "

output_file = open('output1_1.txt', 'w')
output_file.write(str1)
output_file.close()

