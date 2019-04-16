from collections import defaultdict 

class Graph:
	def __init__(self): 
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)


	def dfs(self, v):
		# mark all vertex to not marked
		# recurse marked function

		return 1

	def dfs_marked(self, v, marked):
		marked[v] = True #current node is visited

		#for i in self.graph[v]:
		#if the point has not been marked then go and mark it true



	def bfs(self, v):
		# mark all vertex to not marked
		# create queue
		# mark the origin and enqueue it
		#while queue: dequeue and update by getting all adjacent values that
		#are not marked and mark and enqueue them


		return 1

