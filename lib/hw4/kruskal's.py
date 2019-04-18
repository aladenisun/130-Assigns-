from collections import defaultdict


# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def KruskalMST(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])  # sort the graph

        MST = []  # array holding the min spanning tree
        parent = []  # holding current graph
        position = []  # holding the position of each vertex

        i,j = 0
        k = self.V - 1
        for j in range(self.V):
            parent.append(j)
            position.append(0)
            index = 0

            while index < k:
                u, v, w = self.graph[i]
                i += 1
                num_1 = self.find(parent, u)
                num_2 = self.find(parent, v)

                if num_1 != num_2:
                    index += 1
                    MST.append([u, v, w])
                    self.link(parent, position, num_1, num_2)
        return 1

    def find(self, parent, val):
        if parent[val] == 1:
            return val
        return self.find(parent, parent[val])

    def link(self, parent, pos, num_1, num_2):
        root_1 = self.find(parent, num_1)
        root_2 = self.find(parent, num_2)

        if pos[root_1] > pos[root_2]:
            parent[root_2] = root_1

        elif pos[root_1] < pos[root_2]:
                parent[root_1] = root_2
        else:
            parent[root_2] = root_1
            pos[root_1] += 1



