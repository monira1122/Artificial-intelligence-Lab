import heapq
import math

def star(graph,start,goal,heuristic):
   
    pq=[]
    heapq.heappush(pq,(heuristic[start],0,start,[start]))

    visited={start: 0}

    while pq:
        f,g,node,path=heapq.heappop(pq)
        
        if node==goal:
            return path,g

      
        for neighbour,cost in graph[node]:
            new_g=g+cost
            new_f=new_g+heuristic[neighbour]

        
            if neighbour not in visited or new_g < visited[neighbour]:
                visited[neighbour]=new_g
                heapq.heappush(pq, (new_f,new_g,neighbour,path +[neighbour]))

    return None

graph={
    'S': [('A',1), ('B',5), ('C',8)],
    'A': [('D',3), ('E',7),('G',9)],
    'B': [('G',4)],
    'C': [('G',5)],
    'D': [],
    'E': [],
    'G': []
}

heuristic={
    'S': 8,
    'A': 8,
    'B': 4,
    'C': 3,
    'D': math.inf,
    'E': math.inf,
    'G': 0
}

start=input("Enter source node: ").strip().upper()
goal=input("Enter destination node: ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid nodes")
else:
    result=star(graph,start,goal,heuristic)

    if result:
        path, total_cost=result
        print("\nA* Path:", " → ".join(path))
        print("Total Cost:", total_cost)
    else:
        print("\nNo path found")
