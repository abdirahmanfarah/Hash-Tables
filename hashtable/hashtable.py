class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        # keeps track of the elements in storage
        self.population = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        # str_bytes = key.encode()

        FNV_prime = 2**40 + 2**8 + 0xb3  # 64 bit
        hash = 14695981039346656037
        for i in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(i)
        return hash & 0xffffffffffffffff

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = hash * 33 + ord(x)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # print(self.fnv1(key) % self.capacity)
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.

        0     -> None
        1     -> ("foo",12)
        2     -> ("baz",999) -> ("bar", 99)
        3     -> None
        put("foo", 12)  # hashes to index 1
        put("bar", 30)  # hashes to index 2
        put("baz", 999) # hashes to index 2 <<
        get("beej")     # hashes to index 1
        get("baz")
        delete("bar")
        """

        # rehash_num = divided elem population by capacity number

        # Check if rehash_num is greater than 0.7
        rehash_list = self.population / self.capacity
        load = 0.7

        if rehash_list > load:
            self.resize()

        # Add new entry
        newEntry = HashTableEntry(key, value)
        # hash the key and find it's index
        newIndex = self.hash_index(key)

        # check if newIndex has empty storage
        if self.storage[newIndex] is None:
            self.storage[newIndex] = newEntry
            return
        # get the index storage
        node = self.storage[newIndex]
        # store the value in newIndex
        prev = None
        while node is not None:
            # print(node.key, node.value)
            if node.key == key:
                node.value = newEntry.value
                return
            # go to next node
            prev = node
            node = node.next  # none

        prev.next = newEntry

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.

        0     -> None
        1     -> ("foo",12)
        2     -> ("baz",999) -> ("bar", 99) -> ("beej" 2)
        3     -> None
        put("foo", 12)  # hashes to index 1
        put("bar", 30)  # hashes to index 2
        put("baz", 999) # hashes to index 2 <<
        get("beej")     # hashes to index 1
        get("baz")
        delete("bar")
        """
        # find key using hash index
        index = self.hash_index(key)
        node = self.storage[index]

        if node is None:
            return 'Key not found'

        prev = None

        while node is not None:
            # print(node.key, node.value)
            if node.key == key:
                if prev is None:
                    self.storage[index] = node.next
                    return self.storage[index]
                else:
                    node.next = None
                    return node

                prev = node
            node = node.next
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Find hash index
        index = self.hash_index(key)
        node = self.storage[index]
        # check if node is not None
        while node is not None:
            # if it isn't check if the node key at 0 is the key we want
            if node.key == key:
                # if it is, get the value of the key and break
                return node.value
            # if not, go to the next node
            node = node.next
        # return when the search reaches the end of the single node
        return None

    def resize(self, new_capacity=None):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        curr_storage = self.storage
        self.capacity = new_capacity or self.capacity * 2
        new_array = [None] * self.capacity
        self.storage = new_array
        self.population = 0

        for i in curr_storage:
            if i is not None:
                node = i
                while node is not None:
                    self.put(node.key, node.value)
                    node = node.next

        # if it isn't, do nothing


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
