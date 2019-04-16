from collections import defaultdict 

class Graph:
	def __init__(self): 
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)


	def dfs(self, v):
		# mark all vertex to not marked
		n = len(self.graph)
		marked = [False]* n

		# recurse marked function
		self. dfs_marked(v, marked)
		return 1

	def dfs_marked(self, v, marked):
		marked[v] = True  #current node is visited

		for i in self.graph[v]:
			if marked[i] == False:
				self.dfs_marked(i, marked) #recursive

		#if the point has not been marked then go and mark it true


	def bfs(self, v):
		# mark all vertex to not marked
		n = len(self.graph)
		marked = [False] * n

		# create queue
		Q = []

		# mark the origin and enqueue it
		marked[v] = True
		Q.append(v)

		#while queue: dequeue and update by getting all adjacent values that
		#are not marked and mark and enqueue them
		while Q:
			v = Q.pop(0)
			for i in self.graph[v]:
				if marked[i] == False:
					Q.append(i)
					marked[i] = True
		return 1

