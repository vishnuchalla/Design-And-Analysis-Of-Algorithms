class Sorting:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

    def merge(self, startIdx, midIdx, endIdx):
        leftArrayLength = midIdx - startIdx + 1
        rightArrayLength = endIdx - midIdx
        leftArray = []
        rightArray = []
        for idx in range(0, leftArrayLength):
            leftArray.append(self.sorting_array[idx + startIdx])
        for idx in range(0, rightArrayLength):
            rightArray.append(self.sorting_array[idx + midIdx + 1])
        leftArray.append(float("inf"))
        rightArray.append(float("inf"))
        leftArrayIdx=0
        rightArrayIdx=0
        for outputIdx in range(startIdx, endIdx+1):
            if(leftArray[leftArrayIdx] <= rightArray[rightArrayIdx]):
                self.sorting_array[outputIdx] = leftArray[leftArrayIdx]
                leftArrayIdx += 1
            else:
                self.sorting_array[outputIdx] = rightArray[rightArrayIdx]
                rightArrayIdx += 1
            self.comparison_count += 1

    def merge_sort(self, p, r):
        if(p < r):
            middleIdx = (p + r)//2
            self.merge_sort(p, middleIdx)
            self.merge_sort(middleIdx + 1,r)
            self.merge(p, middleIdx, r)

    def siftDown(self, currentIdx, endIdx):
        while (currentIdx <= endIdx):
            leftChild = currentIdx * 2 + 1
            rightChild = currentIdx * 2 + 2
            idx = currentIdx
            if(leftChild <= endIdx):
                if(self.sorting_array[leftChild] > self.sorting_array[currentIdx]):
                    idx = leftChild
                self.comparison_count += 1
            if(rightChild <= endIdx):
                if(self.sorting_array[rightChild] > self.sorting_array[idx]):
                    idx = rightChild
                self.comparison_count += 1
            if(idx != currentIdx):
                self.sorting_array[idx], self.sorting_array[currentIdx] = self.sorting_array[currentIdx], self.sorting_array[idx]
                currentIdx = idx
            else:
                return

    def max_heapify(self):
        firstParentIdx = (len(self.sorting_array) - 2) // 2
        for idx in range(firstParentIdx, -1, -1):
            self.siftDown(idx, len(self.sorting_array) - 1)

    def heap_sort(self):
        self.max_heapify()
        for idx in range(len(self.sorting_array) - 1, 0, -1):
            self.sorting_array[idx], self.sorting_array[0] = self.sorting_array[0], self.sorting_array[idx]
            self.siftDown(0, idx - 1)

    def insertion_sort(self):
        for idx in range(1, len(self.sorting_array)):
            value = self.sorting_array[idx]
            movingIdx = idx - 1
            while(movingIdx >= 0):
                self.comparison_count += 1
                if(self.sorting_array[movingIdx] > value):
                    self.sorting_array[movingIdx + 1] = self.sorting_array[movingIdx]
                    movingIdx -= 1
                else:
                    break
            self.sorting_array[movingIdx + 1] = value
