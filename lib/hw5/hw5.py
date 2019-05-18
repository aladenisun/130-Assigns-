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

return 1




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