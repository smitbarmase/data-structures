class BinaryHeap:
    def __init__(self):
        self.heap = []

    def isEmpty(self):
        return len(self.heap) == 0

    def clear(self):
        for i in range(len(self.heap)):
            self.heap.pop()

    def size(self):
        return len(self.heap)

    # Returns the value of the element with the lowest
    # priority in this priority queue. If the priority
    # queue is empty null is returned.
    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[0]

    # Removes the root of the heap, O(log(n))
    def poll(self):
        return self.removeAt(0)

    # Test if an element is in heap, O(n)
    def contains(self, element):
        for i in range(len(self.heap)):
            if self.heap[i] == element:
                return True
        return False

    # Adds an element to the priority queue, the
    # element must not be null, O(log(n))
    def add(self, elem):
        if elem != None:
            self.heap.append(elem)
            self.swim(len(self.heap) - 1)
        else:
            print('Invalid element.')
            exit()

    # Tests if the value of node i <= node j
    # This method assumes i & j are valid indices, O(1)
    def less(self, i, j):
        return self.heap[i] < self.heap[j]

    # Perform bottom up node swim, O(log(n))
    def swim(self, k):
        # Grab the index of the next parent node.
        parent = int((k - 1) / 2)

        # Keep swimming while we have not reached the
        # root and while we're less than our parent.
        while k > 0 and self.less(k, parent):
            # Exchange k with the parent
            self.swap(parent, k)
            k = parent

            # Grab the index of the next parent node.
            parent = int((k - 1) / 2)

    # Top down node sink, O(log(n))
    def sink(self, k):
        while True:
            left = (2 * k) + 1 # Left node
            right = (2 * k) + 2 # Right node

            # Assume left is the smallest node of the two children.
            smallest = left

            # Find which is smaller left or right
            # If right is smaller set smallest to be right
            if right < len(self.heap) and self.less(right, left):
                smallest = right

            # Stop if we're outside the bounds of the tree
            # or stop early if we cannot sink k anymore
            if left >= len(self.heap) or self.less(k, smallest):
                break

            # Move down the tree following the smallest node
            self.swap(smallest, k)
            k = smallest

    # Swap two nodes. Assumes i & j are valid, O(1)
    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    # Removes a particular element in the heap, O(n)
    def remove(self, element):
        if (element == None):
            return False
        # Linear removal via search, O(n)
        for i in range(len(self.heap)):
            if element == self.heap[i]:
                self.removeAt(i)
                return True
        return False

    # Removes a node at particular index, O(log(n))
    def removeAt(self, i):
        if self.isEmpty():
            return None

        # To return this data.
        removedData = self.heap[i]

        # Swap it with last element.
        self.swap(i, len(self.heap) - 1)

        # Pop the value.
        self.heap.pop()

        # Getting swaped value in element.
        element = self.heap[i]

        # Try sinking element to satisfy heap variant.
        self.sink(i)

        # If sinking did not work and element still there, try swimming.
        if self.heap[i] == element:
            self.swim(i)

        return removedData

    # This print heap.
    def show(self):
        print(self.heap)

    # Recursively checks if this heap is a min heap.
    # This method is just for testing purposes to make
    # sure the heap invariant is still being maintained.
    # Call this method with k = 0 to start at the root.
    def isMinHeap(self, k):
        # If we are outside the bounds of the heap return true
        if k >= len(self.heap):
            return True

        left = (2 * k) + 1
        right = (2 * k) + 2

        # Make sure that the current node k is less than
        # both of its children left, and right if they exist
        # return false otherwise to indicate an invalid heap
        if left < len(self.heap) and not self.less(k, left):
            return False
        if right < len(self.heap) and not self.less(k, right):
            return False

        # Recurse on both children to make sure they're also valid heaps
        return self.isMinHeap(left) and self.isMinHeap(right)

x = BinaryHeap()
x.add(5)
x.add(3)
x.add(0)
x.add(1)
x.add(4)
x.add(2)
x.removeAt(0)
x.add(6)
x.show()
