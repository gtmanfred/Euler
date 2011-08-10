from abc import ABCMeta, abstractmethod, abstractproperty
 
 
class weighted_graph(metaclass=ABCMeta):
 
    @abstractproperty
    def nodes(self):
        "Get all nodes in the graph."
 
    @abstractproperty
    def edges(self):
        "Get all edges in the graph."
 
    @abstractmethod
    def add(self, e, w=1):
        "Add an edge e = (u, v) with weight w to the graph."
 
    @abstractmethod
    def weight(self, e):
        "Return the weight of the edge e = (u, v)."
 
 
class directed_graph(weighted_graph):
 
    @abstractmethod
    def next_nodes(self, u):
        "Return all nodes that are directly connected by edges starting at u."
 
    @abstractmethod
    def prev_nodes(self, u):
        "Return all nodes that are directly connected by edges ending at u."
 
    def topological_sort(self):
        prev_nodes = self.prev_nodes
        visit = self._visit
        lst = []
        visited = set()
        for u in self.nodes:
            if not prev_nodes(u):
                visit(u, visited, lst)
        lst.reverse()
        return lst
 
    def _visit(self, u, visited, lst):
        visit = self._visit
        if u not in visited:
            visited.add(u)
            for v in self.next_nodes(u):
                visit(v, visited, lst)
            lst.append(u)
 
    def dijkstra(self, queue, *initial_nodes):
        next_nodes = self.next_nodes
        weight = self.weight
        dist = dict((u, 0) for u in initial_nodes)
        prev = dict((u, None) for u in initial_nodes)
        for u in initial_nodes:
            queue.add((0, u))
        while queue:
            d, u = queue.pop()
            for v in next_nodes(u):
                alt = d + weight((u, v))
                if v not in dist:
                    queue.add((alt, v))
                elif alt < dist[v]:
                    queue.decrease_key((dist[v], v), (alt, v))
                else:
                    continue
                dist[v] = alt
                prev[v] = u
        return dist, prev
 
 
class undirected_graph(weighted_graph):
 
    @abstractmethod
    def adjacent_nodes(self, u):
        "Return all nodes that are directly connected with u."
 
    def minimum_spanning_tree(self, queue):
        nodes = self.nodes
        weight = self.weight
        adjacent_nodes = self.adjacent_nodes
        inf = float('inf')
        weights = dict((u, inf) for u in nodes)
        weights[next(iter(nodes))] = 0
        connected_nodes = {}
        for u, w in weights.items():
            queue.add((w, u))
        while queue:
            _, u = queue.pop()
            del weights[u]
            for v in adjacent_nodes(u):
                if v not in weights:
                    continue
                else:
                    w1 = weights[v]
                    w2 = weight((u, v))
                    if w2 < w1:
                        queue.decrease_key((w1, v), (w2, v))
                        weights[v] = w2
                        connected_nodes[v] = u
        return connected_nodes.items()
 
 
class adjacency_list_digraph(directed_graph):
 
    def __init__(self):
        self._nodes = set()
        self._next_nodes = {}
        self._prev_nodes = {}
        self._weights = {}
 
    @property
    def nodes(self):
        return self._nodes
 
    @property
    def edges(self):
        return self._weights.keys()
 
    def add(self, e, w=1):
        nodes = self._nodes
        u, v = e
        nodes.add(u)
        nodes.add(v)
        self._add(u, v, self._next_nodes)
        self._add(v, u, self._prev_nodes)
        self._weights[e] = w
 
    def weight(self, e):
        return self._weights[e]
 
    def next_nodes(self, u):
        next_nodes = self._next_nodes
        return next_nodes[u] if u in next_nodes else []
 
    def prev_nodes(self, u):
        prev_nodes = self._prev_nodes
        return prev_nodes[u] if u in prev_nodes else []
 
    def _add(self, u, v, lists):
        neighbors = lists.setdefault(u, [])
        if v not in neighbors:
            neighbors.append(v)
 
 
class adjacency_list_graph(undirected_graph):
 
    def __init__(self):
        self._nodes = set()
        self._adjacent_nodes = {}
        self._weights = {}
 
    @property
    def nodes(self):
        return self._nodes
 
    @property
    def edges(self):
        return self._weights.keys()
 
    def add(self, e, w=1):
        nodes = self._nodes
        u, v = e
        nodes.add(u)
        nodes.add(v)
        self._add(u, v)
        self._add(v, u)
        self._weights[e if id(u) < id(v) else (v, u)] = w
 
    def weight(self, e):
        if id(e[0]) > id(e[1]):
            e = (e[1], e[0])
        return self._weights[e]
 
    def adjacent_nodes(self, u):
        adjacent_nodes = self._adjacent_nodes
        return adjacent_nodes[u] if u in adjacent_nodes else []
 
    def _add(self, u, v):
        neighbors = self._adjacent_nodes.setdefault(u, [])
        if v not in neighbors:
            neighbors.append(v)