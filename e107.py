from script.collections2 import binary_heap
from script.graphs import adjacency_list_graph
graph = adjacency_list_graph()
with open('script/network.txt') as a_file:
    for i, line in enumerate(a_file):
        for j, x in enumerate(line.strip().split(',')):
            if x != '-':
                graph.add((i, j), int(x))
    tree_edges = graph.minimum_spanning_tree(binary_heap())
    tree_weight = sum(graph.weight(e) for e in tree_edges)
    graph_weight = sum(graph.weight(e) for e in graph.edges)
    print(graph_weight - tree_weight)
