class HashTableEntry:
    """
    Linked List hash table key/value pair.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value


data = [None] * 8


class HashTable:
    def __repr__(self):
        return f'HashTableEntry()'


def my_hashing_function(s):
    string_bytes = s.encode()
    total = 0
    for b in string_bytes:
        total += b
    return total


def get_slot(s):
    hash_val = my_hashing_function(s)
    return hash_val % len(data)


def get(key):
    slot = get_slot(key)
    hash_entry = data[slot]
    if hash_entry is not None:
        return hash_entry.value
    return None


def put(key, value):
    slot = get_slot(key)
    data[slot] = HashTableEntry(key, value)


def delete(key):
    put(key, None)
