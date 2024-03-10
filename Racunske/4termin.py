import queue

graph_simple = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H'],
    'E' : ['G', 'I'],
    'F' : ['J'],
    'G' : ['J'],
    'H' : [],
    'I' : ['J'],
    'J' : []
}

# Traženje po širini

def breadth_first_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    queue_nodes = queue.Queue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    queue_nodes.put(start)
    found_dest = False

    while (not found_dest) and (not queue_nodes.empty()):
        node = queue_nodes.get()
        # print(node)
        for dest in graph[node]:
            if dest not in visited:
                prev_nodes[dest] = node
                if dest is end:
                    found_dest = True
                    break
                visited.add(dest)
                queue_nodes.put(dest)

    path = list()
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()
    return path


path = breadth_first_search(graph_simple, 'A', 'J')
print(path)


# Traženje po dubini

def depth_first_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    stack_nodes = queue.LifoQueue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    stack_nodes.put(start)
    found_dest = False

    while (not found_dest) and (not stack_nodes.empty()):
        node = stack_nodes.get()
        #print(node)
        #for dest in graph[node]:
        for dest in reversed(graph[node]):
            if dest not in visited:
                prev_nodes[dest] = node
                if dest is end:
                    found_dest = True
                    break
                visited.add(dest)
                stack_nodes.put(dest)

    path = list()
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()
    return path

path = depth_first_search(graph_simple, "A", "J")
print(path)

# Traženje planinarenjem

def hill_climbing_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    stack_nodes = queue.LifoQueue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    stack_nodes.put(start)
    found_dest = False

    while (not found_dest) and (not stack_nodes.empty()):
        node = stack_nodes.get()
        #print(node)
        destinations = list()
        for dest in graph[node][1]:
            element = (graph[dest][0], dest)
            destinations.append(element)
        for dest_heur in sorted(destinations, reverse=True):
            if dest_heur[1] not in visited:
                prev_nodes[dest_heur[1]] = node
                if dest_heur[1] is end:
                    found_dest = True
                    break
                visited.add(dest_heur[1])
                stack_nodes.put(dest_heur[1])

    path = list()
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()
    return path

path = hill_climbing_search(graph_simple, "A", "J")
print(path)


# Traženje prvo-najbolji –

def best_first_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    priority_queue = queue.PriorityQueue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    priority_queue.put((graph[start][0], start))
    found_dest = False

    while (not found_dest) and (not priority_queue.empty()):
        node = priority_queue.get()
        #process(node[1])
        for dest in graph[node[1]][1]:
            if dest not in visited:
                prev_nodes[dest] = node[1]
                if dest is end:
                    found_dest = True
                    break
                visited.add(dest)
                priority_queue.put((graph[dest][0], dest))

    path = list()
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()
    return path

path = best_first_search(graph_simple, "A", "J")
print(path)