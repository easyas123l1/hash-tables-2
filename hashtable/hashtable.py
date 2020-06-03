class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        r = ""
        cur = self.head
        while cur is not None:
            r += f'({cur.value})'
            if cur.next is not None:
                r += ' -> '
            cur = cur.next
        return r

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            return current
        while current.next is not None:
            if current.next == value:
                temp = current.next
                current.next = current.next.next
                return temp
            current = current.next
        return None


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity if capacity > 7 else 8
        self.storage = [None] * capacity
        self.items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.items / self.capacity

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity*2)
        # get index of where to store
        index = self.hash_index(key)
        # check if index has been set to a LL if not set it to a LL
        if self.storage[index] is None:
            self.storage[index] = LinkedList()
        # increment count
        self.items += 1
        # on the linked list insert at head a new node hashtableentry
        self.storage[index].insert_at_head(Node(HashTableEntry(key, value)))

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if self.get_load_factor() < 0.2 and self.capacity > 8:
            self.resize(self.capacity // 2)
        # so first find index in storage *the hash*
        index = self.hash_index(key)
        # we will need to search thru the LL to find a node
        ll = self.storage[index]
        # set current to head node
        current = ll.head
        # while current exist
        while current is not None:
            # if current nodes value (memory of hashtableentry)
            if current.value.key == key:
                # return the delete node
                self.items -= 1
                return ll.delete(current.value)
            # increment current
            current = current.next
        # return key not found aka None
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # pretty much same thing as delete...
        index = self.hash_index(key)
        ll = self.storage[index]
        if ll is None:
            return None
        current = ll.head
        while current is not None:
            if current.value.key == key:
                return current.value.value
            current = current.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        self.capacity = new_capacity
        oldStorage = self.storage
        self.storage = [None] * new_capacity
        for x in oldStorage:
            if x is not None:
                current = x.head
                while current is not None:
                    self.put(current.value.key, current.value.value)
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
