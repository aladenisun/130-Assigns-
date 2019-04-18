import sys # Library for INT_MAX 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)]

    def min(self, key, set):
        min = sys.maxint

        for i in range(self.V):
            if key[i] < min and set[i] == False:
                index = key[i]
                index = i
        return index

    def primMST(self):
        key = [sys.maxint]* self.V
        parent = [None] * self.V
        key[0] = 0
        MST = [False]* self.V

        parent[0] = -1

        for count in range(self.V):
            j = self.minKey(key, MST)

            MST[j] = True

            for i in range(self.V):
                if self.graph[j][i] > 0 and MST[i] == False and key[i] > self.graph[j][i]:
                    key[i] = self.graph[j][i]
                    parent[i] = j

        return 1