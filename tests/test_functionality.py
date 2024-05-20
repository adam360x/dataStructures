from minHeap import MinHeap
from maxHeap import MaxHeap

def minHeap():
    
    # Initialize MinHeap of Size 10
    h = MinHeap(10)

    # Insert keys
    h.insertKey(3) 
    h.insertKey(10) 
    h.insertKey(12) 
    h.insertKey(8) 
    h.insertKey(2) 
    h.insertKey(14)

    # Test size
    if h.currSize() != 6:
        print("ERROR: Size Test Failed is: " + str(h.curSize()) + " when should be 6")
        h.printHeap()
        return 1
    
    # Test cur min element
    if h.getMin() != 2:
        print("ERROR: Min Element Test Failed is: " + str(h.getMin()) + " when should be 2")
        h.printHeap()
        return 1
    
    # insert more
    h.insertKey(1)
    h.insertKey(100)

    # Test cur min element
    if h.getMin() != 1:
        print("ERROR: Min Element Test Failed is: " + str(h.getMin()) + " when should be 1")
        h.printHeap
        return 1
    
    # Test size
    if h.currSize() != 8:
        print("ERROR: Size Test Failed is: " + str(h.curSize()) + " when should be 8")
        h.printHeap()
        return 1

    return 0

def maxHeap():
    
    # Initialize MaxHeap of Size 10
    h = MaxHeap(10)

    # Insert keys
    h.insertKey(3) 
    h.insertKey(10) 
    h.insertKey(12) 
    h.insertKey(8) 
    h.insertKey(2) 
    h.insertKey(14)

    # Test size
    if h.currSize() != 6:
        print("ERROR: Size Test Failed is: " + str(h.curSize()) + " when should be 6")
        h.printHeap()
        return 1
    
    # Test cur max element
    if h.getMax() != 14:
        print("ERROR: Max Element Test Failed is: " + str(h.getMax()) + " when should be 14")
        h.printHeap()
        return 1
    
    # insert more
    h.insertKey(1)
    h.insertKey(100)

    # Test cur max element
    if h.getMax() != 100:
        print("ERROR: Max Element Test Failed is: " + str(h.getMax()) + " when should be 100")
        h.printHeap()
        return 1
    
    # Test size
    if h.currSize() != 8:
        print("ERROR: Size Test Failed is: " + str(h.curSize()) + " when should be 8")
        h.printHeap()
        return 1

    return 0



def test_all():
    assert minHeap() == 0
    assert maxHeap() == 0