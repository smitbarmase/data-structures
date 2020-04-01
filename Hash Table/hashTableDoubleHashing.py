import hashTableOpenAddressingBase as base
import sympy # To check prime number

class HashTableDoubleHashing(base._HashTableOpenAddressingBase):
    __hash = 1

    def __init__(self, capacity = 7, loadFactor = 0.35):
        super().__init__(capacity, loadFactor)

    def _secHash(self, key):
        return hash(key) + 1

    def __setupProbing(key):
        # Cache second hash value.
        self.__hash = self.__normalizeIndex(self._secHash(key))

        # Fail safe to avoid infinite loop.
        if self.__hash == 0:
            self.__hash = 1

    def _probe(self, x):
        return x * self.__hash

    # Adjust the capacity until it is a prime number. The reason for
    # doing this is to help ensure that the GCD(hash, capacity) = 1 when
    # probing so that all the cells can be reached.
    def _adjustCapacity(self):
        while sympy.isprime(self.capacity) == False:
            self.capacity += 1

# Program
x = HashTableDoubleHashing()
x.add('A', 3)
x.add('B', 4)
x.add('C', 6)
x.add('D', 8)
x.add('E', 9)
x.add('F', 10)
x.remove('D')
x.show()
