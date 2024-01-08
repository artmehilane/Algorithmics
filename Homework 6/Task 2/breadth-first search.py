def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:  # Loop to visit each node
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.append(vertex)  # Mark the vertex as visited
            queue.extend([n for n in graph[vertex] if n not in visited])

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bfs(graph, 'A'))

# Output will be the order in which the nodes are visited.

#Used materials on BFS from datagy.io to learn from and get help to complete this task

#A.Mehilane and R.Priske
