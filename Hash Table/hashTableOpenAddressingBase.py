# Base class for hashtables with an open addressing collision resolution method,
# such as linear probing, quadratic probing and double hashing.

class _HashTableOpenAddressingBase:
    # Constructor
    def __init__(self, capacity = 7, loadFactor = 0.65):
        self.loadFactor = loadFactor # Factor to decide when to double capacity.
        self.capacity = max(capacity, 7) # Number of buckets in table.
        self.threshold = int(self.capacity * self.loadFactor) # Max entries can be fitted.]

        self.keys = [None for i in range(self.capacity)]
        self.values = [None for i in range(self.capacity)]

        self.usedBuckets = 0
        self.keyCount = 0
        self.modificationCount = 0

    # These three methods are used to dictate how the probing is to actually
    # occur for whatever open addressing scheme you are implementing.
    def _setupProbing(self, key):
        pass

    def _probe(self, x):
        pass

    # Adjusts the capacity of the hash table after it's been made larger.
    # This is important to be able to override because the size of the hashtable
    # controls the functionality of the probing function.
    def _adjustCapacity(self):
        pass


    # Increase capacity of Hash Table
    def _increaseCapacity(self):
        self.capacity = (self.capacity * 2) + 1

    def clear(self):
        self.keys = [None for i in range(self.capacity)]
        self.values = [None for i in range(self.capacity)]
        self.keyCount = self.usedBuckets = 0
        self.modificationCount += 1

    # Returns the number of keys currently inside the hash-table
    def size(self):
        return self.keyCount

    # Returns the capacity of the hashtable (used mostly for testing)
    def getCapacity(self):
        return self.capacity

    def isEmpty(self):
        return self.keyCount == 0

    def put(self, key, value):
        return self.insert(key, value)

    def add(self, key, value):
        return self.insert(key, value)

    def containsKey(self, key):
        return self.hasKey(key)

    # Returns a list of keys found in the hash table
    def keys(self):
        hashtableKeys = []
        for i in range(self.capacity):
            if self.keys[i] != None and self.keys[i] != 'TOMBSTONE':
                hashtableKeys.append(self.keys[i])
        return hashtableKeys

    # Returns a list of values found in the hash table
    def values(self):
        hashtableValues = []
        for i in range(self.capacity):
            if self.keys[i] != None and self.keys[i] != 'TOMBSTONE':
                hashtableValues.append(self.values[i])
        return hashtableValues

    # Double the size of the hash-table
    def _resizeTable(self):
        self._increaseCapacity()
        self._adjustCapacity()

        self.threshold = int(self.capacity * self.loadFactor)

        oldKeyTable = [None for i in range(self.capacity)]
        oldValueTable = [None for i in range(self.capacity)]

        # Perform key table pointer swap
        keyTableTmp = self.keys
        self.keys = oldKeyTable
        oldKeyTable = keyTableTmp

        # Perform value table pointer swap
        valueTableTmp = self.values
        self.values = oldValueTable
        oldValueTable = valueTableTmp

        # Reset the key count and buckets used since we are about to
        # re-insert all the keys into the hash-table.
        self.keyCount = self.usedBuckets = 0

        for i in range(len(oldKeyTable)):
            if oldKeyTable[i] != None and oldKeyTable[i] != 'TOMBSTONE':
                self.insert(oldKeyTable[i], oldValueTable[i])
            oldValueTable[i] = None
            oldKeyTable[i] = None

    # Converts a hash value to an index. Essentially, this strips the
    # negative sign and places the hash value in the domain [0, capacity)
    def _normalizeIndex(self, keyHash):
        return abs(keyHash) % self.capacity

    # Finds the greatest common denominator of a and b.
    def _gcd(self, a, b):
        if b == 0:
            return a
        return self._gcd(b, a % b)

    # Place a key-value pair into the hash-table. If the value already
    # exists inside the hash-table then the value is updated
    def insert(self, key, val):
        if key == None:
            raise Exception('Null Key')
        if self.usedBuckets >= self.threshold:
            self._resizeTable()

        self._setupProbing(key)
        offset = self._normalizeIndex(hash(key))

        i = offset
        j = -1
        x = 1

        while True:
            # The current slot was previously deleted
            if self.keys[i] == 'TOMBSTONE':
                if j == -1:
                    j = i
            # The current cell already contains a key
            elif self.keys[i] != None:
                # The key we're trying to insert already exists in the hash-table,
                # so update its value with the most recent value
                if self.keys[i] == key:
                    oldValue = self.values[i]
                    if j == -1:
                        self.values[i] = val
                    else:
                        self.keys[i] = 'TOMBSTONE'
                        self.values[i] = None
                        self.keys[j] = key
                        self.values[j] = val
                    self.modificationCount += 1
                    return oldValue
            # Current cell is null so an insertion/update can occur
            else:
                # No previously encountered deleted buckets
                if j == -1:
                    self.usedBuckets += 1
                    self.keyCount += 1
                    self.keys[i] = key
                    self.values[i] = val

                    # Previously seen deleted bucket. Instead of inserting
                    # the new element at i where the null element is insert
                    # it where the deleted token was found.
                else:
                    self.keyCount += 1
                    self.keys[j] = key
                    self.values[j] = val
                self.modificationCount += 1
                return None
            i = self._normalizeIndex(offset + self._probe(x))
            x += 1

    # Returns true/false on whether a given key exists within the hash-table
    def hasKey(self, key):
        if key == None:
            raise Exception('Null key')

        self._setupProbing(key)
        offset = self._normalizeIndex(hash(key))

        # Starting at the original hash linearly probe until we find a spot where
        # our key is or we hit a null element in which case our element does not exist.
        i = offset
        j = -1
        x = 1
        while True:
            # Ignore deleted cells, but record where the first index
            # of a deleted cell is found to perform lazy relocation later.
            if self.keys[i] == 'TOMBSTONE':
                if j == -1:
                    j = i
            # We hit a non-null key, perhaps it's the one we're looking for.
            elif self.keys[i] != None:
                # The key we want is in the hash-table!
                if self.keys[i] == key:
                    # If j != -1 this means we previously encountered a deleted cell.
                    # We can perform an optimization by swapping the entries in cells
                    # i and j so that the next time we search for this key it will be
                    # found faster. This is called lazy deletion/relocation.
                    if j != -1:
                        # Swap the key-value pairs of positions i and j.
                        self.keys[j] = self.keys[i]
                        self.values[j] = self.values[i]
                        self.keys[i] = 'TOMBSTONE'
                        self.values[i] = None
                    return True
            # Key was not found in the hash-table :/
            else:
                return False
            i = self._normalizeIndex(offset + self._probe(x))
            x += 1

    # Get the value associated with the input key.
    def get(self, key):
        if key == None:
            raise Exception('Null key')

        self._setupProbing(key)
        offset = self._normalizeIndex(hash(key))

        # Starting at the original hash linearly probe until we find a spot where
        # our key is or we hit a null element in which case our element does not exist.
        i = offset
        j = -1
        x = 1
        while True:
            # Ignore deleted cells, but record where the first index
            # of a deleted cell is found to perform lazy relocation later.
            if self.keys[i] == 'TOMBSTONE':
                if j == -1:
                    j = i
            # We hit a non-null key, perhaps it's the one we're looking for.
            elif self.keys[i] != None:
                # The key we want is in the hash-table!
                if self.keys[i] == key:
                    # If j != -1 this means we previously encountered a deleted cell.
                    # We can perform an optimization by swapping the entries in cells
                    # i and j so that the next time we search for this key it will be
                    # found faster. This is called lazy deletion/relocation.
                    if j != -1:
                        # Swap the key-value pairs of positions i and j.
                        self.keys[j] = self.keys[i]
                        self.values[j] = self.values[i]
                        self.keys[i] = 'TOMBSTONE'
                        self.values[i] = None
                        return self.values[j]
                    else:
                        return self.values[i]
            # element was not found in the hash-table :/
            else:
                return None
            i = self._normalizeIndex(offset + self._probe(x))
            x += 1

    # Removes a key from the map and returns the value.
    def remove(self, key):
        if key == None:
            raise Exception('Null key')

        self._setupProbing(key)
        offset = self._normalizeIndex(hash(key))

        # Starting at the original hash linearly probe until we find a spot where
        # our key is or we hit a null element in which case our element does not exist.
        i = offset
        x = 1
        while True:
            # Ignore deleted cells.
            if self.keys[i] == 'TOMBSTONE':
                pass

            # Key was not found in hash-table.
            if self.keys[i] == None:
                return None

            # The key we want is in the hash-table!
            if self.keys[i] == key:
                    self.keyCount -= 1
                    self.modificationCount += 1
                    oldValue = self.values[i]
                    self.keys[i] = 'TOMBSTONE'
                    self.values[i] = None
                    return oldValue

            i = self._normalizeIndex(offset + self._probe(x))
            x += 1

    def show(self):
        result = {}
        for key, value in zip(self.keys, self.values):
            if key != None and key != 'TOMBSTONE':
                result.update({key : value})
        print(result)
