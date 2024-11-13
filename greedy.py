import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'

def greedy_best_first_search(graph, start, goal, heuristic):

    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    
    visited = set()
    
    while priority_queue:
        
        _, current_node = heapq.heappop(priority_queue)
        
        
        if current_node == goal:
            return True
        visited.add(current_node)       

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
    
    return False

print(greedy_best_first_search(graph, start, goal, heuristic))
 