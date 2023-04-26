def bellman_ford(graph, start):
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}

    # Relax all edges |V| - 1 times
    for i in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node

    # Check for negative-weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances, predecessors

graph = {
    'A': {'B': 3, 'C': 5},
    'B': {'C': -2, 'D': 1},
    'C': {'B': 4, 'D': 2},
    'D': {}
}

start = 'A'

distances, predecessors = bellman_ford(graph, start)

for node in graph:
    print(f"The shortest distance from {start} to {node} is: {distances[node]}")
    path = []
    current_node = node
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()
    print(f"The shortest path is: {path}")
