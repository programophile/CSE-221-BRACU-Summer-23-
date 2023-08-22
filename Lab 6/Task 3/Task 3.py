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
        if curr_node is None:
            return distance_node

        visited.add(curr_node)

        for neighbor, danger in graph[curr_node].items():
            new_distance = max(distance_node[curr_node], danger)
            if new_distance < distance_node[neighbor]:
                distance_node[neighbor] = new_distance

    return distance_node


input_file = open('input3_1.txt', 'r')
n, m = map(int, input_file.readline().split())
graph = {i: {} for i in range(1, n + 1)}

for _ in range(m):
    u, v, w = map(int, input_file.readline().split())
    graph[u][v] = w

distances = dijkstra(graph, start=1)
destination_distance = distances[n]


if destination_distance == float('inf'):
    result = "Impossible"
else:
    result = destination_distance


output_file = open('output3_1.txt', 'w')
output_file.write(str(result))
output_file.close()
