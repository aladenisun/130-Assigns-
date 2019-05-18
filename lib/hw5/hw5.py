class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()
    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(to_node, length)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge

class Node:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, to_node, length):
        self.to_node = to_node
        self.length = length

def dijkstra(graph, source):
    visited = {source: 0}
    dist = {}

    nodes = set(graph.nodes)

    while nodes:
        min = None
        for node in nodes:
            if node in visited:
                if min is None:
                    min = node
                elif visited[node] < visited[min]:
                    min = node

        if min is None:
            break

        nodes.remove(min)
        recent_weight = visited[min]

        for edge in graph.edges[min]:
            weight = recent_weight + graph.distance[(min,edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                dist[edge] = min

    return visited, dist

def BellmanFord(graph, source):
     d, p = initialize(graph, source)
     for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)

     for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]
     return d, p

def Ford_fullerskon(graph, source, sink):    # you can implement Bfs or dfs to get the path from source(start node) to sink(end node)
    flow, path = 0, True
    debug = None
    while path:
        path, reserve = depth_first_search(graph, source, sink)
        flow += reserve

        for v, u in zip(path, path[1:]):
            if graph.has_edge(v, u):
                graph[v][u]['flow'] += reserve
            else:
                graph[u][v]['flow'] -= reserve

        if callable(debug):
            debug(graph, path, reserve, flow)
    return 1


def depth_first_search(graph, source, sink):
    undirected = graph.to_undirected()
    explored = {source}
    stack = [(source, 0, undirected[source])]

    while stack:
        v, _, neighbours = stack[-1]
        if v == sink:
            break

        # search the next neighbour
        while neighbours:
            u, e = neighbours.popitem()
            if u not in explored:
                break
        else:
            stack.pop()
            continue

        # current flow and capacity
        in_direction = graph.has_edge(v, u)
        capacity = e['capacity']
        flow = e['flow']

        # increase or redirect flow at the edge
        if in_direction and flow < capacity:
            stack.append((u, capacity - flow, undirected[u]))
            explored.add(u)
        elif not in_direction and flow:
            stack.append((u, flow, undirected[u]))
            explored.add(u)

    # (source, sink) path and its flow reserve
    reserve = min((f for _, f, _ in stack[1:]), default=0)
    path = [v for v, _, _ in stack]
    return path, reserve


def initialize(graph, source):
    d = {}
    p = {}

    for node in graph:
        d[node] = float ('Inf')
        p[node] = None
    d[source] = 0
    return d, p

def relax(node, neighbour, graph, d, p):
    if d[neighbour] > d[node] + graph[node][neighbour]:
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node