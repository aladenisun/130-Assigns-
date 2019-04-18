from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def topologicalSortUtil(self, v, marked, stack):
        marked[v] = True

        for i in self.graph[v]:
            if marked[i] == False:
                self.topologicalSortUtil(i, marked,stack)

                stack.insert(0,v)


    def topological_Sort(self):
        marked = [False]*self.V
        stack = []

        for i in range(self.V):
            if marked[i] == False:
                self.topologicalSortUtil(i, marked,stack)

        return 1

    def position(self, v, marked, stack):
        marked[v] = True
        for i in self.graph[v]:
            if marked[i] == False:
                self.position(i, marked, stack)

        stack = stack.append(v)

    def Transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g

    def SCC(self):    # strongly connected components
        stack = []
        marked = [False]*(self.V)
        for i in range(self.V):
            if marked[i] == False:
                self.position(i, marked, stack)

        gph = self.Transpose()

        marked= [False]*(self.V)

        while stack:
            i = stack.pop()
            if marked[i] == False:
                gph.topologicalSortUtil(i, marked, stack)

        return 1