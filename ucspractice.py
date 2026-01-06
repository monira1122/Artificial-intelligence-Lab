import heapq

def ucs(graph,start,goal):
    queue=[(0,start,[start])]
    visited=set()
    
    while queue:
        cost,node,path=heapq.heappop(queue)
        
        if node==goal:
            return path,cost
        
        if node not in visited:
            visited.add(node)
            
            for neighbour,weight in graph[node].items():
                if neighbour not in visited:
                    heapq.heappush(
                        queue,(cost+weight,neighbour,path+[neighbour])
                    )
    return None

graph = {
    'S': {'A': 5, 'B': 2, 'C': 4},
    'A': {'D': 9, 'E': 4},
    'B': {'G': 6},
    'C': {'F': 2},
    'D': {'H': 7},
    'E': {'G': 6},
    'F': {'G': 1},
    'G': {},
    'H': {}
}

start = input("Enter source node: ").strip().upper()
goal  = input("Enter destination node: ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid nodes! Please enter valid nodes from the graph.")
else:
    result = ucs(graph, start, goal)
    
    if result:
        path, total_cost = result
        print("\nUCS Path:", " → ".join(path))
        print("Total Cost:", total_cost)
        
    else:
        print("\nNo path found using UCS.")