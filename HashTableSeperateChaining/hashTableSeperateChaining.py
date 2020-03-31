class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = key.hashCode()

    def equals(self, other):
        if self.hash != other.hash:
            return False
        return self.key == other.keys

    def toString(self):
        return self.key + ' => ' + self.value

class HashTableSeparateChaining:
    # Constructor
    def __init__(self, capacity = 3, loadFactor = 0.75):
        self.capacity = max(capacity, 3)
        self.loadFactor = max(loadFactor, 0.75)

    # Returns the number of elements currently inside the hash-table
    def getSize(self):
        return self.size

    # Returns true/false depending on whether the hash-table is empty
    def isEmpty(self):
        return self.size == 0

    # Converts a hash value to an index. Essentially, this strips the
    # negative sign and places the hash value in the domain [0, capacity)
    def normalizeIndex(self, keyHash):
        return abs(keyHash) % self.capacity;

    # Clears all the contents of the hash-table
    def clear(self):
        Arrays.fill(table, None)
        self.size = 0

    def containsKey(self, key):
        return self.hasKey(key)

    # Returns true/false depending on whether a key is in the hash table
    def hasKey(self, key):
        bucketIndex = self.normalizeIndex(key.hashCode())
        return self.bucketSeekEntry(bucketIndex, key) != None

    # Insert, put and add, all place a value in the hash-table
    def put(self, key, value):
        return self.insert(key, value)

    def add(self, key, value):
        return self.insert(key, value)

    def insert(self, key, value):
        if key == None:
            raise Exception('Null key')
        newEntry = Entry(key, value)
        bucketIndex = self.normalizeIndex(newEntry.hash)
        return self.bucketInsertEntry(bucketIndex, newEntry)

    # Gets a key's values from the map and returns the value.
    def get(self, key):
        if key == None:
            return None
        bucketIndex = self.normalizeIndex(key.hashCode())
        entry = self.bucketSeekEntry(bucketIndex, key)
        if entry != None:
            return entry.value
        return None

    # Removes a key from the map and returns the value.
    def remove(self, key):
        if key == None:
            return None
        bucketIndex = self.normalizeIndex(key.hashCode())
        return self.__bucketRemoveEntry(bucketIndex, key)

    # Removes an entry from a given bucket if it exists
    def __bucketRemoveEntry(self, bucketIndex, key):
        entry = self.bucketSeekEntry(bucketIndex, key)
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
        if bucket == None:
            self.table[bucketIndex] = bucket = []

        existentEntry = self.bucketSeekEntry(bucketIndex, entry.key)
        if existentEntry == None:
            bucket.add(entry)
            if self.size + 1 > self.threshold:
                self.resizeTable()
            return None
            # Use None to indicate that there was no previous entry
        else:
            oldVal = existentEntry.value
            existentEntry.value = entry.value
            return oldVal

    # Finds and returns a particular entry in a given bucket if it exists, returns null otherwise
    def __bucketSeekEntry(self, bucketIndex, key):
        if (key == null) return null;
        LinkedList<Entry<K, V>> bucket = table[bucketIndex];
        if (bucket == null) return null;
        for (Entry<K, V> entry : bucket) if (entry.key.equals(key)) return entry;
        return null;
  }
