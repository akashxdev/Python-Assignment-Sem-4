# define function to find the parent of a node
def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

# define function to perform union of two nodes
def union(parent, rank, x, y):
    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# define Kruskal's algorithm function
def kruskal(graph, vertices):
    edges = []
    result = []
    for i in range(vertices):
        for j in range(i+1, vertices):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))
    edges.sort()
    parent = []
    rank = []
    for node in range(vertices):
        parent.append(node)
        rank.append(0)
    i = 0
    while len(result) < vertices - 1:
        weight, x, y = edges[i]
        i += 1
        xroot = find_parent(parent, x)
        yroot = find_parent(parent, y)
        if xroot != yroot:
            result.append((x, y, weight))
            union(parent, rank, xroot, yroot)
    return result

# example usage
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

vertices = len(graph)
result = kruskal(graph, vertices)

# print the result
print("Akash Sarkar")
for edge in result:
    print(edge[0], '-', edge[1], ':', edge[2])
