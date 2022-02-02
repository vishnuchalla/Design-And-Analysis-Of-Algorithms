#DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
class Dijkstra:


	def Dijkstra_alg(self, n, e, mat, s):
		 #Write your code here to calculate shortest paths and usp values from source to all vertices
		 #This method will have four inputs (Please see testcase file)
		 #This method should return a two dimensional array as output (Please see testcase file)
		 edges = [[] for i in range(n)]
		 for each in range(e):
		 	edges[mat[each][0] - 1].append([mat[each][1] - 1, mat[each][2]])
		 	edges[mat[each][1] - 1].append([mat[each][0] - 1, mat[each][2]])
		 return self.dijkstrasAlgorithm(s-1, edges)

	def dijkstrasAlgorithm(self, start, edges):
		vertices = len(edges)

		minimumDistances = [[float("inf"), 0] for i in range(vertices)]
		minimumDistances[start] = [0, 1]
		minimumDistancesHeap = MinHeap([(idx, float("inf")) for idx in range(vertices)])
		minimumDistancesHeap.update(start, 0)

		while not minimumDistancesHeap.isEmpty():
			vertex, currentDistance = minimumDistancesHeap.remove()

			if currentDistance == float("inf"):
				break

			for edge in edges[vertex]:
				destination, distance = edge

				newDistance = currentDistance + distance
				currentPathDistance = minimumDistances[destination][0]
				if newDistance < currentPathDistance:
					minimumDistances[destination] = [newDistance, minimumDistances[vertex][1]]
					minimumDistancesHeap.update(destination, newDistance)
				elif newDistance == currentPathDistance:
					minimumDistances[destination][1] = 0

		solution = []
		for eachDistance in range(len(minimumDistances)):
			if minimumDistances[eachDistance][0] == float("inf"):
				solution.append([-1, 0])
			else:
				solution.append(minimumDistances[eachDistance])
		return solution

class MinHeap:
	def __init__(self, array):
		self.indexMap = {index: index for index in range(len(array))}
		self.heap = self.buildHeap(array)

	def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2
		for i in range(firstParentIdx, -1, -1):
			self.shiftDown(i, len(array) - 1, array)
		return array

	def shiftDown(self, currentIndex, endIndex, array):
		while (currentIndex <= endIndex):
			leftChild = currentIndex * 2 + 1
			rightChild = currentIndex * 2 + 2
			index = currentIndex
			if(leftChild <= endIndex and array[leftChild][1] < array[currentIndex][1]):
				index = leftChild
			if(rightChild <= endIndex and array[rightChild][1] < array[index][1]):
				index = rightChild
			if(index != currentIndex):
				self.swap(currentIndex, index, array)
				currentIndex = index
			else:
				return

	def shiftUp(self, currentIndex, array):
		parentIndex = (currentIndex - 1) // 2
		while(currentIndex > 0 and array[parentIndex][1] > array[currentIndex][1]):
			self.swap(currentIndex, parentIndex, array)
			currentIndex = parentIndex
			parentIndex = (currentIndex - 1) // 2

	def update(self, vertex, vertexValue):
		self.heap[self.indexMap[vertex]] = (vertex, vertexValue)
		self.shiftUp(self.indexMap[vertex], self.heap)

	def remove(self):
		if self.isEmpty():
			return
		self.swap(0, len(self.heap) - 1, self.heap)
		index, minimumDistance = self.heap.pop()
		self.indexMap.pop(index)
		self.shiftDown(0, len(self.heap) - 1, self.heap)
		return index, minimumDistance

	def isEmpty(self):
		return len(self.heap) == 0

	def swap(self, first, second, array):
		self.indexMap[array[first][0]] = second
		self.indexMap[array[second][0]] = first
		array[first], array[second] = array[second], array[first]
