class MinHeap:
    
    def __init__(self, maxSize: int) -> None:
        self.maxSize = maxSize
        self.curSize = 0
        # Because we have a heap (complete binary tree) we can store in array
        self.heap = [None] * maxSize

    def insertKey(self, key: int) -> None:
        
        # Currently, we just return if heap is full
        if self.curSize == self.maxSize:
            print("ERROR: Heap Full, exiting\n")
            return
        
        # Insert element at end of array        
        self.heap[self.curSize] = key      
        self.curSize += 1

        index = self.curSize - 1
        parent = (self.curSize - 1) // 2

        # Worst case for this while loop is O(log(n))
        while(self.heap[index] < self.heap[parent]):
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            index = parent
            parent = (index - 1) // 2
            if parent < 0:
                break

    def currSize(self) -> int:
        return self.curSize
    
    def getMin(self) -> int:
        return self.heap[0]
    
    def printHeap(self):
        print(self.heap)
    