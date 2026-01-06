from collections import deque

# ------------------------------------------------------
# BFS search where user gives source and destination
# ------------------------------------------------------

def bfs(graph, start, goal):
    queue = deque([(start, [start], 0)])   # (current_node, path, total_cost)
    visited = set()
    tested_node=0
    while queue:
        
        node, path, cost = queue.popleft()   # FIFO → BFS

        

        if node not in visited:
          
            
            
          visited.add(node)
          tested_node+=1
          
        if node == goal:
            
          
            return path, cost,tested_node
          

        for neighbour, edge_cost in graph[node]:
                if neighbour not in visited:
                    queue.append(
                        (neighbour, path + [neighbour], cost + edge_cost)
                    )

    return None


# ------------------------------------------------------
# Same Graph WITH costs
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

start = input("Enter source: ").strip().upper()
goal  = input("Enter goal: ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid node! Please enter valid nodes.")
else:
    result = bfs(graph, start, goal)

    if result:
        
            
          
        path, total_cost,tested_node= result
        print("\nBFS Path:", " -> ".join(path))
        print("Total Cost:",total_cost)
        
        print("Tested node", tested_node)
    else:
        print("Path not found")
