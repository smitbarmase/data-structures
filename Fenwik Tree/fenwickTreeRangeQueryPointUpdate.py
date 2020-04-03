class FenwickTreeRangeQueryPointUpdate:
    def __init__(self, arg):
        if type(arg) == int: # Take size as argument.
            self.N = arg + 1
            self.tree = [None for i in range(self.N)]

        elif type(arg) == list: # Take values one - based list as argument.
            if list == None:
                raise Exception('Values array cannot be null!')
            else:
                self.N = len(arg)
                self.tree = arg
                for i in range(self.N):
                    parent = i + self._lsb(i)
                    if parent < self.N:
                        self.tree[parent] += self.tree[i]
        else:
            raise Exception('Invalid Argument.')

    # Returns the value of the least significant bit (LSB)
    # lsb(108) = lsb(0b1101100) =     0b100 = 4
    # lsb(104) = lsb(0b1101000) =    0b1000 = 8
    # lsb(96)  = lsb(0b1100000) =  0b100000 = 32
    # lsb(64)  = lsb(0b1000000) = 0b1000000 = 64
    def _lsb(self, i):
        # Isolates the lowest one bit value
        return i & -i

    # Computes the prefix sum from [1, i], O(log(n))
    def _prefixSum(self, i):
        sum = 0
        while i != 0:
            sum += self.tree[i]
            i &= ~self._lsb(i) # Equivalently, i -= lsb(i);
        return sum

    # Returns the sum of the interval [left, right], O(log(n))
    def sum(self, left, right):
        if right < left:
            raise Exception('Make sure right >= left')
        return self._prefixSum(right) - self._prefixSum(left - 1)

    # Get the value at index i
    def get(self, i):
        return self.sum(i, i)

    # Add 'v' to index 'i', O(log(n))
    def add(self, i, v):
        while i < self.N:
            self.tree[i] += v
            i += self._lsb(i)

    # Set index i to be equal to v, O(log(n))
    def set(self, i, v):
        self.add(i, v - self.sum(i, i))

    # Print
    def show(self):
        print('Tree: ', self.tree)

# Program
# This class takes argument size or list. IMPORTANT - Should be one - based.
x = FenwickTreeRangeQueryPointUpdate([0, 2, 3, 4, 5, 8, 7]) # First element will not be taken.
x.set(4, 6)
print('Element at index 4 is: ', x.get(4))
print('Element at index 2 is: ', x.get(2))
