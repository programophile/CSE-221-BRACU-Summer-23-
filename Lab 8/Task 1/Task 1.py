# def find_parent(parents, node):
#     if parents[node] == node:
#         return node
#     parents[node] = find_parent(parents, parents[node])
#     return parents[node]
#
#
# def union(parents, ranks, u, v):
#     root_u = find_parent(parents, u)
#     root_v = find_parent(parents, v)
#
#     if root_u != root_v:
#         if ranks[root_u] < ranks[root_v]:
#             parents[root_u] = root_v
#         else:
#             parents[root_v] = root_u
#             if ranks[root_u] == ranks[root_v]:
#                 ranks[root_u] += 1
#
#
# def minimum_maintenance_cost(N, graph):
#     parents = list(range(N + 1))
#     ranks = [0] * (N + 1)
#
#     edges = []
#     for u in graph:
#         for v, w in graph[u]:
#             edges.append((u, v, w))
#
#     edges.sort(key=lambda x: x[2])
#
#     total_cost = 0
#     edge_count = 0
#     for u, v, w in edges:
#         if find_parent(parents, u) != find_parent(parents, v):
#             union(parents, ranks, u, v)
#             total_cost += w
#             edge_count += 1
#             if edge_count == N - 1:
#                 break
#
#     for u, v, w in edges:
#         if find_parent(parents, u) != find_parent(parents, v):
#             total_cost += w
#
#     return total_cost
#
#
# # Read input
# N, M = map(int, input().split())
# graph = {i: [] for i in range(1, N + 1)}
# for _ in range(M):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))
#     graph[v].append((u, w))
#
# # Calculate and print the minimum maintenance cost achievable
# result = minimum_maintenance_cost(N, graph)
# print(result)
def read_input(file_obj):
    first_line = file_obj.readline().split()
    num_cities, num_roads = int(first_line[0]), int(first_line[1])
    road_data = []
    connections = {}
    for i in range(num_cities + 1):
        connections[i] = [i]
    for _ in range(num_roads):
        road_info = file_obj.readline().split()
        city1, city2, cost = int(road_info[0]), int(road_info[1]), int(road_info[2])
        road_data.append([city1, city2, cost])
    return road_data, connections, num_cities

def calculate_min_cost(road_data, connections, num_cities):
    total_cost = 0
    for city1, city2, cost in road_data:
        if city1 not in connections[city2] or city2 not in connections[city1]:
            combined = connections[city1] + connections[city2]
            combined = list(set(combined))
            for node in combined:
                connections[node] = combined
            total_cost += cost
            if len(connections[city1]) == num_cities:
                break
    return total_cost

def output(file_obj, result):
    output_file = open(file_obj, "w")
    output_file.write(str(result))
    output_file.close()

def input_output(input_file, output_file):
    with open(input_file, "r") as f:
        road_data, connections, num_cities = read_input(f)
        road_data.sort(key=lambda x: x[2])
        min_cost = calculate_min_cost(road_data, connections, num_cities)
        output(output_file, min_cost)

input_output('Input1_1.txt', 'Output1_1.txt')
input_output('Input1_2.txt', 'Output1_2.txt')
