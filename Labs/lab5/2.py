#from display import display2

from functools import reduce
from matplotlib.pyplot import show
from networkx import Graph, draw_kamada_kawai

colors = {
    'R': "#FF0000",
    'G': "#00FF00",
    'B': "#0000FF",
    'Y': "#FFFF00",
    'P': "#FF00FF",
    "C": "#00FFFF",
}


def display(graph, data):
    col = [0] * len(data)
    for n in data:
        col[int(n[0]) - 1] = colors[n[1]]
    G = Graph()
    G.add_nodes_from([str(x) for x in range(1, len(data) + 1)])
    G.add_edges_from(list(
        reduce(lambda acc, el: acc + [(el[0], x) for x in el[1]],
               [(key, val) for (key, val) in graph.items()],
               [])
    ))
    draw_kamada_kawai(G,
                      with_labels=True,
                      node_size=2000,
                      font_size=16,
                      node_color=col)
    show()
    
def display2(graph, mapped):
    col = [0] * len(mapped)
    for key in mapped.keys():
        col[ord(key) - ord('A')] = colors[mapped[key]]
    G = Graph()
    G.add_nodes_from(graph.keys())
    G.add_edges_from([(x, y) for x in graph.keys() for y in graph[x]])
    draw_kamada_kawai(G,
                      with_labels=True,
                      node_size=2000,
                      font_size=16,
                      node_color=col)
    show()

#from display import display2

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'E', 'B'],
    'D' : ['B', 'E'],
    'E' : ['C', 'D']
}

colors = set({ 'R', 'G', 'B' })

def backtracting_with_forward_checking_and_mvr(G, c):
    stack = [{
        'uncolored' : list(G.keys()),
        'domain' : { x: list(c) for x in G.keys() },
        'colored': {},
        'prev': None
    }]
    solution = None
    while stack and not solution:
        top, *stack = stack
        if not top['uncolored']:
            solution = top['colored']
        else:
            to_color = top['uncolored'][0]
            potential = list(top['domain'][to_color])
            for n in G[to_color]:
                if top['colored'].get(n, None) and top['colored'][n] in potential:
                    potential.remove(top['colored'][n])
            if potential:
                newDomain = dict(top['domain'])
                newDomain[to_color] = potential
                for n in G[to_color]:
                    if potential[0] in newDomain[n]:
                        newDomain[n].remove(potential[0])
                stack.append({
                    'uncolored': sorted([x for x in top['uncolored'] if x is not to_color], key=lambda x: len(newDomain[x])),
                    'domain': newDomain,
                    'colored': top['colored'] | { to_color: potential[0] },
                    'prev': top
                })
            elif top['prev']:
                stack.append(top['prev'])
    return solution

sol = backtracting_with_forward_checking_and_mvr(graph, colors)
print(sol)
if sol:
    display2(graph, sol)