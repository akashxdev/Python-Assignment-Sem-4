from heapq import heappop, heappush

def prim(graph, start):
    visited = set()
    heap = [(0, start)]
    while heap:
        (weight, vertex) = heappop(heap)
        if vertex in visited:
            continue
        visited.add(vertex)
        yield vertex, weight
        for neighbor, w in graph[vertex].items():
            if neighbor not in visited:
                heappush(heap, (w, neighbor))
                
# Example usage
graph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 15, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}
start_vertex = 'A'
print("Akash Sarkar")
print(list(prim(graph, start_vertex)))
