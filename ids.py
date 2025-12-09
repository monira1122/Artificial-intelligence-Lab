# ---------------------------------------------------
# Depth-Limited DFS (helper for IDS)
# ---------------------------------------------------
def depth_limited_dfs(graph, node, goal, depth, path, total_cost, visited):
    if depth == 0:
        if node == goal:
            return path, total_cost
        return None

    visited.add(node)

    for neighbour, cost in graph[node]:
        if neighbour not in visited:
            result = depth_limited_dfs(
                graph,
                neighbour,
                goal,
                depth - 1,
                path + [neighbour],
                total_cost + cost,
                visited.copy()
            )
            if result is not None:
                return result

    return None


# ---------------------------------------------------
# IDS (Iterative Deepening Search)
# ---------------------------------------------------
def ids(graph, start, goal):
    max_depth = len(graph)

    for depth in range(max_depth):
        visited = set()
        result = depth_limited_dfs(
            graph, start, goal, depth,
            [start], 0, visited
        )
        if result is not None:
            return result

    return None


# ---------------------------------------------------
# Graph WITH costs
# Child ordering changed so S → B explored first
# ---------------------------------------------------
graph = {
    'S': [('B',2), ('A',5), ('C',4)],   # <<< B প্রথমে
    'A': [('D',9), ('E',4)],
    'B': [('G',6)],
    'C': [('F',2)],
    'D': [('H',7)],
    'E': [('G',6)],
    'F': [('G',1)],
    'G': [],
    'H': []
}


# ---------------------------------------------------
# User Input
# ---------------------------------------------------
start = input("Enter source node: ").strip().upper()
goal = input("Enter destination node: ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid nodes! Please enter valid nodes from the graph.")
else:
    result = ids(graph, start, goal)

    if result:
        path, total_cost = result
        print("\nIDS Path:", " → ".join(path))
        print("Total Cost:", total_cost)
    else:
        print("\nNo path found using IDS.")
