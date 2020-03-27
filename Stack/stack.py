class Stack:
    # Node class inside stack
    class Node:
        # Node constructor
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next

    # Stack constructor
    def __init__(self):
        self.head = None
        self.size = 0

    # Push element at head in stack, O(1)
    def push(self, data):
        if self.head == None:
            self.head = self.Node(data)
        else:
            temp = self.Node(data, self.head)
            self.head = temp
        self.size += 1

    # Pop element from stack at top, O(1)
    def pop(self):
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
        print('Stack:', end = ' ')
        while temp != None:
            print(temp.data, end = ' ')
            temp = temp.next

x = Stack()
x.push(2)
x.push(3)
x.push(4)
x.push(6)
x.push(7)
x.pop()
x.pop()
x.show()
