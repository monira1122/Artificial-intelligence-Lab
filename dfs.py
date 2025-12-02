# ------------------------------------------------------
# DFS search where user gives source and destination
# ------------------------------------------------------

def dfs(graph, start, goal):
    stack = [(start, [start])]   # (current_node, path)
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            # Push neighbours in REVERSE order so DFS visits left child first
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append((neighbour, path + [neighbour]))

    return None


# ------------------------------------------------------
# Graph (E before D under A)
# ------------------------------------------------------

graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E'],   # E first → ensures path S-A-E-G
    'B': ['G'],
    'C': ['F'],
    'D': ['H'],
    'E': ['G'],
    'F': ['G'],
    'G': [],
    'H': []
}


# ------------------------------------------------------
# User Input
# ------------------------------------------------------

start = input("Enter source node: ").strip().upper()
goal = input("Enter destination node: ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid nodes! Please enter valid nodes from the graph.")
else:
    path = dfs(graph, start, goal)

    if path:
        print("\nDFS Path:", " → ".join(path))
    else:
        print("\nNo path found using DFS.")
