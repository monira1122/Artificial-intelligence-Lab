# ------------------------------------------------------
# DFS search where user gives source and destination
# ------------------------------------------------------

def dfs(graph, start, goal):
    stack = [(start, [start], 0)]   # (current_node, path, total_cost)
    visited = set()

    while stack:
        node, path, cost = stack.pop()

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            # Push neighbours in REVERSE order so DFS visits left child first
            for neighbour, edge_cost in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(
                        (neighbour, path + [neighbour], cost + edge_cost)
                    )

    return None


# ------------------------------------------------------
# Graph WITH costs
# ------------------------------------------------------

graph = {
    'S': [('A',5), ('B',2), ('C',4)],
    'A': [('D',9), ('E',4)],
    'B': [('G',6)],
    'C': [('F',2)],
    'D': [('H',7)],
    'E': [('G',6)],
    'F': [('G',1)],
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
    result = dfs(graph, start, goal)

    if result:
        path, total_cost = result
        print("\nDFS Path:", " → ".join(path))
        print("Total Cost:", total_cost)
    else:
        print("\nNo path found using DFS.")
