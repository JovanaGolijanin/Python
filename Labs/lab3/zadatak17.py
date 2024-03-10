
import queue

graph_simple = {
'A' : [('B',8),('C',5)],  #tuple jer treba da ukljucuje i rastojanje izmedju dva cvora
'B' : [('A',8),('D',10), ('E',9)],
'C' : [('A',5),('F',3), ('G',2)],
'D' : [('B',10),('H',4)],
'E' : [('B',9),('G',1), ('I',6)],
'F' : [('C',3),('J',4)],
'G' : [('C',2),('E',1),('J',3)],
'H' : [('D',4)],
'I' : [('E',6),('J',2)],
'J' : [('F',4),('G',3),('I',2)]
}

# initial_graph = {
#   'A': [('B', 2), ('C', 5)],
#   'B': [('A', 2), ('E', 3)],
#   'C': [('A', 5), ('F', 9), ('G', 3)],
#   'D': [('F', 1)],
#   'E': [('B', 3), ('G', 4)],
#   # 'E': [('B', 3)],
#   'F': [('C', 9), ('D', 1), ('G', 4)],
#   'G': [('E', 4), ('F', 4), ('C', 3)],
#   'H': []
# }

def breadth_first_search(graph,end):
    queue_nodes = queue.Queue(len(graph))
    visited = set()
    prev_nodes = dict()
    graph_with_heuristic = dict()
    graph_with_heuristic[end] = (0, graph[end])
    prev_nodes[end] = None
    visited.add(end)
    queue_nodes.put(end)  

    while (not queue_nodes.empty()):
        node = queue_nodes.get()
       
        for dest in graph[node]:
            if dest[0] not in visited:
                graph_with_heuristic[dest[0]] = (graph_with_heuristic[node][0] + dest[1], graph[dest[0]])
                prev_nodes[dest[0]] = node
                visited.add(dest[0])
                queue_nodes.put(dest[0]) 
            else:
                if graph_with_heuristic[dest[0]][0] > graph_with_heuristic[node][0] + dest[1]:
                        graph_with_heuristic[dest[0]] = (graph_with_heuristic[node][0] + dest[1],graph[dest[0]]) 
                        queue_nodes.put(dest[0]) 

        for node in graph.keys():
            if node not in visited:
                graph_with_heuristic[node] = (None, graph[node])
    return graph_with_heuristic                                   

graph_result = breadth_first_search(graph_simple, 'G')

print(graph_result)
for el in graph_result.keys():
    print(f"( {el} , {graph_result[el][0]} )")