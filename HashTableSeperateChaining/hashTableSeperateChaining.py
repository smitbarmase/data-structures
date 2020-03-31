class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)

    def equals(self, other):
        if self.hash != other.hash:
            return False
        return self.key == other.keys

    def toString(self):
        return self.key + ' => ' + self.value

class HashTableSeparateChaining:
    # Constructor
    def __init__(self, capacity = 3, maxLoadFactor = 0.75):
        self.maxLoadFactor = maxLoadFactor # Factor to decide when to double capacity.
        self.capacity = max(capacity, 3) # Number of buckets in table.
        self.threshold = int(self.capacity * self.maxLoadFactor) # Max entries can be fitted.
        self.table = [[] for i in range(self.capacity)]
        self.size = 0 # Current number of entries in table.

    # Returns the number of elements currently inside the hash-table
    def getSize(self):
        return self.size

    # Returns true/false depending on whether the hash-table is empty
    def isEmpty(self):
        return self.size == 0

    # Converts a hash value to an index. Essentially, this strips the
    # negative sign and places the hash value in the domain [0, capacity)
    def __normalizeIndex(self, keyHash):
        return abs(keyHash) % self.capacity;

    # Clears all the contents of the hash-table
    def clear(self):
        self.table = [[] for i in range(self.capacity)]
        self.size = 0

    def containsKey(self, key):
        return self.hasKey(key)

    # Returns true/false depending on whether a key is in the hash table
    def hasKey(self, key):
        bucketIndex = self.__normalizeIndex(hash(key))
        return self.__bucketSeekEntry(bucketIndex, key) != None

    # Insert, put and add, all place a value in the hash-table
    def put(self, key, value):
        return self.insert(key, value)

    def add(self, key, value):
        return self.insert(key, value)

    def insert(self, key, value):
        if key == None:
            raise Exception('Null key')
        newEntry = Entry(key, value)
        bucketIndex = self.__normalizeIndex(newEntry.hash)
        return self.__bucketInsertEntry(bucketIndex, newEntry)

    # Gets a key's values from the map and returns the value.
    def get(self, key):
        if key == None:
            return None
        bucketIndex = self.__normalizeIndex(hash(key))
        entry = self.__bucketSeekEntry(bucketIndex, key)
        if entry != None:
            return entry.value
        return None

    # Removes a key from the map and returns the value.
    def remove(self, key):
        if key == None:
            return None
        bucketIndex = self.__normalizeIndex(hash(key))
        return self.__bucketRemoveEntry(bucketIndex, key)

    # Removes an entry from a given bucket if it exists
    def __bucketRemoveEntry(self, bucketIndex, key):
        entry = self.__bucketSeekEntry(bucketIndex, key)
        if entry != None:
            links = self.table[bucketIndex]
            links.remove(entry)
            self.size -= 1
            return entry.value
        else:
            return None

    # Inserts an entry in a given bucket only if the entry does not already
    # exist in the given bucket, but if it does then update the entry value
    def __bucketInsertEntry(self, bucketIndex, entry):
        bucket = self.table[bucketIndex]

        existentEntry = self.__bucketSeekEntry(bucketIndex, entry.key)
        if existentEntry == None:
            bucket.append(entry)
            if self.size + 1 > self.threshold:
                self.__resizeTable()
            return None
            # Use None to indicate that there was no previous entry
        else:
            oldVal = existentEntry.value
            existentEntry.value = entry.value
            return oldVal

    # Finds and returns a particular entry in a given bucket if it exists, returns null otherwise
    def __bucketSeekEntry(self, bucketIndex, key):
        if key == None:
            return None
        bucket = self.table[bucketIndex]
        if bucket == []:
            return None
        for entry in bucket:
            if entry.key == key:
                return entry
        return None

    # Resizes the internal table holding buckets of entries
    def __resizeTable(self):
        self.capacity *= 2
        self.threshold = int(self.capacity * self.maxLoadFactor)

        newTable = [[] for i in range(self.capacity)]

        for i in range(len(self.table)):
            if self.table[i] != []:
                for entry in self.table[i]:
                    bucketIndex = self.normalizeIndex(entry.hash)
                    bucket = newTable[bucketIndex]
                    bucket.append(entry)

                #Avoid memory leak. Help the GC
                self.table[i] = None

        self.table = newTable

    # Returns the list of keys found within the hash table
    def keys(self):
        keysList = []
        for bucket in self.table:
            if bucket != None:
                for entry in bucket:
                    keysList.append(entry.key)
        return keysList

    # Returns the list of values found within the hash table
    def values(self):
        valuesList = []
        for bucket in self.table:
            if bucket != None:
                for entry in bucket:
                    valuesList.append(entry.value)
        return valuesList

    def show(self):
        result = {entry.key : entry.value for bucket in self.table for entry in bucket}
        print(result)

# Linked list can be use for chaining. Here, we have used python list.
# Program here
x = HashTableSeparateChaining(4)
x.insert('A', 20)
x.insert('B', 40)
x.insert('D', 60)
x.insert('C', 80)
x.insert('E', 20)
x.remove('D')
x.show()
