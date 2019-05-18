class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []
        
    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
            self.neighbors.sort()

    def add_neighbors(self, neighbors):
      for neighbor in neighbors:
            if isinstance(neighbor, Vertex):
                if neighbor.name not in self.neighbors:
                    self.neighbors.append(neighbor.name)
                    neighbor.neighbors.append(self.name)
                    self.neighbors = sorted(self.neighbors)
                    neighbor.neighbors = sorted(neighbor.neighbors)
            else: return False
        
    def __repr__(self):
        return str(self.neighbors)

class Graph:
    def __init__(self):
        self.vertices = {} #vertices dictionary
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
          self.vertices[vertex.name] = vertex
          return True
        else: return False

    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex,Vertex):
                self.vertices[vertex.name] = vertex.neighbors
            
    def add_edge(self, vertex_from, vertex_to):
        if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
            for i, value in self.vertices.items():
                if i == vertex_from:
                    vertex_from.add_neighbor(vertex_from)
                if i == vertex_to:
                    vertex_to.add_neighbor(vertex_to)
            return True
        else:
            return False
           # vertex_from.add_neighbor(vertex_to)
            #if isinstance(vertex_from, Vertex) and isinstance(vertex_to, Vertex):
             #  self.vertices[vertex_from.name] = vertex_from.neighbors
              #  self.vertices[vertex_to.name] = vertex_to.neighbors

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    
    def adjacencyList(self): # to represent the graph as adjacent list  
        if len(self.vertices) >= 1:
            return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]
        else:
            return dict()

                        
def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyList()) + '\n'