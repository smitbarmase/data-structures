class DoublyLinkedList:
    # Node class inside linked list
    class Node:
        # Node constructor
        def __init__(self, data = None, prev = None, next = None):
            self.data = data
            self.prev = prev
            self.next = next

    # Linked list constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Insert element at last in linked list, O(n)
    def insert(self, data):
        if self.head == None:
            self.head = self.tail = self.Node(data)
        else:
            temp = self.Node(data)
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
        self.size += 1

    # Remove element at given index in linked list, O(n)
    def removeAt(self, index):
        if index < 0 or index > self.size - 1:
            print('Error')
        elif index == 0:
            temp = self.head
            self.head = temp.next
            temp.next.prev = None
            del temp
            self.size -= 1
        elif index == self.size - 1:
            temp = self.tail
            self.tail = temp.prev
            temp.prev.next = None
            del temp
            self.size -= 1
        else:
            if index <= (self.size // 2):
                temp = self.head
                for i in range(1, index):
                    temp = temp.next
                toDelete = temp.next
                temp.next = toDelete.next
                temp.next.prev = temp
                del toDelete
            else:
                temp = self.tail
                for i in range(self.size - index, self.size - 1, -1):
                    temp = temp.prev
                toDelete = temp.prev
                temp.prev = toDelete.prev
                temp.prev.next = temp
                del toDelete
            self.size -= 1

    # Remove last element in linked list, O(n)
    def remove(self):
        self.removeAt(self.size - 1)

    # Returns size of linked list, O(1)
    def getSize(self):
        return self.size

    # Find the index of a particular value in the linked list, O(n)
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

    # Check is a value is contained within the linked list
    def contains(self, data):
        return self.indexOf(data) != -1

    # Print linked list
    def show(self):
        temp = self.head
        print('List:', end = ' ')
        while temp != None:
            print(temp.data, end = ' ')
            temp = temp.next

x = DoublyLinkedList()
x.insert(2)
x.insert(3)
x.insert(4)
x.insert(6)
x.insert(7)
x.removeAt(0)
x.removeAt(3)
x.show()
