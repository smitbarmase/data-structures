class SinglyLinkedList:
    # Node class inside linked list
    class Node:
        # Node constructor
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next

    # Linked list constructor
    def __init__(self):
        self.head = None
        self.size = 0

    # Insert element at last in linked list, O(n)
    def insert(self, data):
        if self.head == None:
            self.head = self.Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = self.Node(data)
        self.size += 1

    # Remove element at given index in linked list, O(n)
    def removeAt(self, index):
        if index < 0 or index > self.size - 1:
            print('Error')
        elif index == 0:
            temp = self.head
            self.head = temp.next
            del temp
            self.size -= 1
        else:
            temp = self.head
            for i in range(1, index):
                temp = temp.next
            toDelete = temp.next
            temp.next = toDelete.next
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

x = SinglyLinkedList()
x.insert(2)
x.insert(3)
x.insert(4)
x.insert(6)
x.insert(7)
x.removeAt(2)
x.remove()
x.show()
