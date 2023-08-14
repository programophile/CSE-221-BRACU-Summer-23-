import math
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

        if curr_node == None:
            return distance_node

        visited.add(curr_node)

        for neighbor, weight in graph[curr_node].items():
            distance = distance_node[curr_node] + weight
            if distance < distance_node[neighbor]:
                distance_node[neighbor] = distance

    return distance_node


# Read input
input_file = open('input2_3.txt', 'r')
n, m = map(int, input_file.readline().split())
graph = {i: {} for i in range(1, n + 1)}

for _ in range(m):
    u, v, w = map(int, input_file.readline().split())
    graph[u][v] = w
start_a, start_b = map(int, input_file.readline().split())

# Calculate meeting point
distances_a = dijkstra(graph, start_a)
distances_b = dijkstra(graph, start_b)
# print(distances_b,distances_a)

min_meeting_time = float('inf')
meeting_node = -1
min_time=math.inf
for node in graph:
    # print(node)
    if max(distances_a[node],distances_b[node]) < min_time and (distances_b[node]!= math.inf or distances_a[node]!= math.inf):

        # min_meeting_time = distances_a[node] + distances_b[node]
        # print(min_meeting_time)
        min_time=max(distances_b[node],distances_a[node])
        meeting_node = node
        # print(meeting_node)

if min_time == float('inf'):
    result = "Impossible"
else:
    result = (min_time, meeting_node)


output_file = open('output2_3.txt', 'w')
if result == "Impossible":
    output_file.write(result)
else:
    output_file.write(f"Time {result[0]}\nNode {result[1]}")
output_file.close()
