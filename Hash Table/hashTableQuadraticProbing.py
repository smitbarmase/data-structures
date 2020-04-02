#An implementation of a hash-table using open addressing with quadratic probing as a collision
# resolution method.
#
# <p>In this implementation we are using the following probing function: H(k, x) = h(k) + f(x) mod
# 2^n
#
# <p>Where h(k) is the hash for the given key, f(x) = (x + x^2) / 2 and n is a natural number. We
# are using this probing function because it is guaranteed to find an empty cell (i.e it generates
# all the numbers in the range [0, 2^n) without repetition for the first 2^n numbers).

import hashTableOpenAddressingBase as base
from math import log

class HashTableQuadraticProbing(base._HashTableOpenAddressingBase):

    def __init__(self, capacity = 7, loadFactor = 0.35):
        super().__init__(capacity, loadFactor)

    def _highestOneBit(self, n):
        # To find the position of the most significant set bit
        k = int(log(n, 2))
        # To return the value of the number with set bit at k-th position
        return 2**k

    # Given a number this method finds the next
    # power of two above this value.
    def __nextPowerOfTwo(self, n):
        return self._highestOneBit(n) << 1

    # No setup required for quadratic probing.
    def __setupProbing(self, key):
        pass

    def _probe(self, x):
        #Quadratic probing function (x^2+x)/2
        return (x * x + x) >> 1

    # Increase the capacity of the hashtable to the next power of two.
    def _increaseCapacity(self):
        self.capacity = self.__nextPowerOfTwo(self.capacity)

    # Adjust the capacity of the hashtable to be a power of two.
    def _adjustCapacity(self):
        pow2 = self._highestOneBit(self.capacity)
        if self.capacity == pow2:
            return
        self._increaseCapacity()

# Program
x = HashTableQuadraticProbing()
x.add('A', 3)
x.add('B', 4)
x.add('C', 6)
x.add('D', 8)
x.add('E', 9)
x.add('F', 10)
x.remove('D')
x.show()
