class BinarySearchTree:
    class Node:
        # Node constructor
        def __init__(self, left, right, data):
            self.left = left
            self.right = right
            self.data = data

    # Binary search tree class
    def __init__(self):
        self.nodeCount = 0
        self.root = None

    # compareTo(a, b) returns -1 if a < b, 0 if a == b, 1 if a > b
    def compareTo(self, aData, bData):
        if aData < bData:
            return -1
        elif aData == bData:
            return 0
        else:
            return +1

    # Check if this binary tree is empty
    def isEmpty(self):
        return self.size() == 0

    # Get the number of nodes in this binary tree
    def size(self):
        return self.nodeCount

    # Add an element to this binary tree. Returns true
    # if we successfully perform an insertion
    def add(self, data):
        # Check if the value already exists in this
        # binary tree, if it does ignore adding it
        # Otherwise add this element to the binary tree
        if self.contains(data):
            return False
        else:
          self.root = self.__add(self.root, data)
          self.nodeCount += 1
          return True

    # Private method to recursively add a value in the binary tree
    def __add(self, node, data):
        # Base case: found a leaf node
        if node == None:
            node = self.Node(None, None, data)
        else:
            # Pick a subtree to insert element
            if self.compareTo(data, node.data) < 0:
                node.left = self.__add(node.left, data)
            else:
                node.right = self.__add(node.right, data)
        return node

    # Remove a value from this binary tree if it exists, O(n)
    def remove(self, data):
        # Make sure the node we want to remove
        # actually exists before we remove it
        if self.contains(data):
            self.root = self.__remove(self.root, data)
            self.nodeCount -= 1
            return True
        return False

    # Private remove method.
    def __remove(self, node, data):
        if node == None:
            return None

        cmp = self.compareTo(data, node.data)

        # Dig into left subtree, the value we're looking
        # for is smaller than the current value
        if cmp < 0:
            node.left = self.__remove(node.left, data)
            # Dig into right subtree, the value we're looking
            # for is greater than the current value
        elif cmp > 0:
            node.right = self.__remove(node.right, data)
            # Found the node we wish to remove
        else:
            # We find the value.

            # Case with only a right subtree or no subtree at all.
            # In this situation just swap the node we wish to remove with its right child.
            if node.left == None:
                rightChild = node.right
                node.data = None
                node = None

                return rightChild

            # Case with only a left subtree or no subtree at all.
            # In this situation just swap the node we wish to remove with its left child.
            elif node.right == None:
                leftChild = node.left
                node.data = None
                node = None

                return leftChild

            # When removing a node from a binary tree with two links the
            # successor of the node being removed can either be the largest
            # value in the left subtree or the smallest value in the right
            # subtree. In this implementation I have decided to find the
            # smallest value in the right subtree which can be found by
            # traversing as far left as possible in the right subtree.
            else:
                # Find the leftmost node in the right subtree
                tmp = self.findMin(node.right)

                # Swap the data
                node.data = tmp.data

                # Go into the right subtree and remove the leftmost node we
                # found and swapped data with. This prevents us from having
                # two nodes in our tree with the same value.
                node.right = self.__remove(node.right, tmp.data)

                # If instead we wanted to find the largest node in the left
                # subtree as opposed to smallest node in the right subtree
                # here is what we would do:
                # tmp = self.findMax(node.left)
                # node.data = tmp.data
                # node.left = self.__remove(node.left, tmp.data)
        return node

    # Helper method to find the leftmost node (which has the smallest value)
    def findMin(self, node):
        while node.left != None:
            node = node.left
        return node

    # Helper method to find the rightmost node (which has the largest value)
    def findMax(self, node):
        while node.right != None:
            node = node.right
        return node

    # returns true is the element exists in the tree
    def contains(self, data):
        return self.__contains(self.root, data)

    # private recursive method to find an element in the tree
    def __contains(self, node, data):
        # Base case: reached bottom, value not found
        if node == None:
            return False

        cmp = self.compareTo(data, node.data)

        #Dig into the left subtree because the value we're
        # looking for is smaller than the current value
        if cmp < 0:
            return self.__contains(node.left, data)

        # Dig into the right subtree because the value we're
        # looking for is greater than the current value
        elif cmp > 0:
            return self.__contains(node.right, data)

        # We found the value we were looking for
        else:
            return True

    # Computes the height of the tree, O(n)
    def height(self):
        return self.__height(self.root)

    # Recursive helper method to compute the height of the tree
    def __height(self, node):
        if node == None:
            return 0
        return max(self.__height(node.left), self.__height(node.right)) + 1

    # This method returns an iterator for a given TreeTraversalOrder.
    # The ways in which you can traverse the tree are in four different ways:
    # preorder, inorder, postorder and levelorder.
    def traverse(self, order):
        result = []
        if order == 'PRE_ORDER':
            self.__preOrderTraversal(self.root, result)
        elif order == 'IN_ORDER':
            self.__inOrderTraversal(self.root, result)
        elif order == 'POST_ORDER':
            self.__postOrderTraversal(self.root, result)
        elif order == 'LEVEL_ORDER':
            self.__levelOrderTraversal([self.root], result)
        else:
            return 'Wrong Order'
        return result

    def __preOrderTraversal(self, root, result):
        if root == None:
            return
        result.append(root.data)
        self.__preOrderTraversal(root.left, result)
        self.__preOrderTraversal(root.right, result)

    def __inOrderTraversal(self, root, result):
        if root == None:
            return
        self.__inOrderTraversal(root.left, result)
        result.append(root.data)
        self.__inOrderTraversal(root.right, result)

    def __postOrderTraversal(self, root, result):
        if root == None:
            return
        self.__postOrderTraversal(root.left, result)
        self.__postOrderTraversal(root.right, result)
        result.append(root.data)

    def __levelOrderTraversal(self, current, result):
        if current == []:
            return
        nextLevel = []
        for node in current:
            result.append(node.data)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        self.__levelOrderTraversal(nextLevel, result)

# Program starts here.
# traverse(str) -> str: 'PRE_ORDER', 'IN_ORDER', 'POST_ORDER', 'LEVEL_ORDER'
x = BinarySearchTree()
x.add(7)
x.add(5)
x.add(9)
x.add(10)
x.add(11)
x.remove(7)
x.add(4)
x.add(6)
x.add(8)
print(x.traverse('IN_ORDER'))
