import hashTableOpenAddressingBase as base

class HashTableLinearProbing(base._HashTableOpenAddressingBase):
    # This is the linear constant used in the linear probing, it can be
    # any positive number. The table capacity will be adjusted so that
    # the GCD(capacity, LINEAR_CONSTANT) = 1 so that all buckets can be probed.
    __LINEAR_CONSTANT = 17

    def __init__(self, capacity = 7, loadFactor = 0.65):
        super().__init__(capacity, loadFactor)

    def _probe(self, x):
        return self.__LINEAR_CONSTANT * x

    # Adjust the capacity so that the linear constant and
    # the table capacity are relatively prime.
    def _adjustCapacity(self):
        while self._gcd(self.__LINEAR_CONSTANT, self.capacity) != 1:
            self.capacity += 1

# Program
x = HashTableLinearProbing()
x.add('A', 3)
x.add('B', 4)
x.add('C', 6)
x.add('D', 8)
x.add('E', 9)
x.add('F', 10)
x.remove('D')
x.show()
