class UnionFind:
    def __init__(self, size):
        # Used to track the size of each of the component
        self.sz = []

        # id[i] points to the parent of i, if id[i] = i then i is a root node.
        self.id = []

        # Initialization
        for i in range(size):
            self.sz.append(1)
            self.id.append(i)

    # Find which component/set 'p' belongs to, takes amortized constant time.
    def find(self, p):
        # Find the root of the component/set
        root = p
        while root != self.id[root]:
            root = self.id[root]

        # Compress the path leading back to the root.
        # Doing this operation is called "path compression"
        # and is what gives us amortized time complexity.
        while p != root:
            next = self.id[p]
            self.id[p] = root
            p = next

        return root


    # Return whether or not the elements 'p' and
    # 'q' are in the same components/set.
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # Return the size of the components/set 'p' belongs to
    def componentSize(self, p):
        return self.sz[find(p)]

    # Return the number of elements in this UnionFind/Disjoint set
    def size(self):
        count = 0
        for i in range(len(self.sz)):
            count += self.sz[i]
        return count

    # Returns the number of remaining components/sets
    def components(self):
        return len(self.sz)

    # Unify the components/sets containing elements 'p' and 'q'
    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        # These elements are already in the same group!
        if root1 == root2:
            return

        # Merge smaller component/set into the larger one.
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.sz[root1] = 0
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.sz[root2] = 0
            self.id[root2] = root1

    def show(self):
        print('Size:', self.sz)
        print('Id:', self.id)

# Program here >
x = UnionFind(8)
x.unify(6, 7) # 6 <- 7
x.unify(5, 6) # 6 <- 5
x.unify(4, 5) # 6 <- 4
x.unify(3, 4) # 6 <- 3
x.unify(0, 1) # 0 <- 1
x.unify(1, 2) # 0 <- 2
x.unify(1, 5) # 6 <- 0  ~ Component of 6 is greater than component of 0
x.show()
