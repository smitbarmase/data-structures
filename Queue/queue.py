class Queue:
    # Node class inside queue
    class Node:
        # Node constructor
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next

    # Queue constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Enqueue element at tail in queue, O(1)
    def enqueue(self, data):
        if self.head == None:
            self.head = self.tail = self.Node(data)
        else:
            temp = self.Node(data)
            self.tail.next = temp
            self.tail = temp
        self.size += 1

    # Dequeue element from head in queue, O(1)
    def dequeue(self):
        temp = self.head
        self.head = self.head.next
        del temp
        self.size -= 1

    # Returns size of linked list, O(1)
    def getSize(self):
        return self.size

    # Find the index of a particular value in stack, O(n)
    def indexOf(self, data):
        index = 0
        temp = self.head
        while index < self.size:
            if temp.data == data:
                return index
            temp = temp.next
            index += 1
        else:
            return -1

    # Check is a value is contained within the stack
    def contains(self, data):
        return self.indexOf(data) != -1

    # Print stack
    def show(self):
        temp = self.head
        print('Queue:', end = ' ')
        while temp != None:
            print(temp.data, end = ' ')
            temp = temp.next

x = Queue()
x.enqueue(2)
x.enqueue(3)
x.enqueue(4)
x.enqueue(6)
x.enqueue(7)
x.dequeue()
x.dequeue()
x.show()
