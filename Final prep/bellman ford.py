def bellman_ford(graph, source):
    # Initialize distances
    distance = {vertex: float('inf') for vertex in graph}
    distance[source] = 0

    # Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u]:
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    # Check for negative weight cycles
    for u in graph:
        for v, w in graph[u]:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                print("Graph contains negative weight cycle")
                return

    # Print distances
    print("Vertex  Distance from Source")
    for vertex, dist in distance.items():
        print(f"{vertex}\t\t{dist}")

# Example usage
graph = {
    0: [(1, -1), (2, 4)],
    1: [(2, 3), (3, 2), (4, 2)],
    3: [(2, 5), (1, 1)],
    4: [(3, -3)]
}

source_vertex = 0
bellman_ford(graph, source_vertex)
