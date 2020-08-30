#!/usr/bin/python

# Hashmap with fixed size and linear probing
#
# Along with quadratic probing and double hashing,
# linear probing is a form of open addressing.
#
# Article: https://en.wikipedia.org/wiki/Linear_probing
#

# Open addressing: all entry records are stored in the bucket itself.
# but the location ("address") of the item is not determined by its hash value.
#
# Collision solutions: use probe sequences like linear probing, quadratic probing, double hashing
#
# For Linear probling: https://en.wikipedia.org/wiki/Linear_probing
#
# 1. Each cell of a hash table stores a single key-value pair.
# 2. When the hash function causes a collision by mapping a new key to a cell of the hash table that is already occupied by another key, linear probing searches the table for the closest following free location and inserts the new key there.
# 3. Lookups are performed in the same way, by searching the table sequentially starting at the position given by the hash function, until finding a cell with a matching key or an empty cell.

# Hash function selections:
#
# 1. Provide a uniform distribution of hash values. difficult to ensure by design, but may be evaluated by statistical tests.
# 2. For open addressing, need avoid clustering.
# 3. Cryptograghic hash function provide good hash functions for any table size by modulo reduction or by bit masking. but offen slower to compute. a non-cryptographic hash function might be preferable, like DJB2, FNV1a, etc.

# Key statistics:
#
# Load factor = n/k
#
# n: the number of occupied entries in the hash table
# n: the number of all buckets
#
# As the load factor grows larger, the hash table becomes slower, and it may even fail to work.

CAPACITY = 256

LINEAR_PROBING=0
QUADRATIC_PROBING=1
DOUBLE_HASH=2

import hashlib

class HashMap:
    def __init__(self,capacity=CAPACITY,probe_mode=LINEAR_PROBING):
        self.capacity = capacity
        self.array = [ [] for i in range(capacity) ]
        self.probe_mode = probe_mode
        self.count = 0

    def _hash(self, key):
        return int(hashlib.md5(str(key).encode('utf-8')).hexdigest(), 16) % len(self.array)

    # Returns:
    # -1:    means: the hashmap is full, could not find the key
    # index: means: if array[index] is blank, means could not find the key.
    #               else means find the key.
    def _get_index(self, key):
        index = self._hash(key)
        orig_index = index
        while self.array[index] and self.array[index][0] != key:
            # Linear probing
            index = (index + 1) % len(self.array)
            if index == orig_index:
                # Hash table is full, could not find the key
                return -1

        return index

    def exists(self, key):
        index = self._get_index(key)
        return index != -1 and bool(self.array[index])

    def get(self, key):
        index = self._get_index(key)
        if index == -1 or not self.array[index]:
            return None

        return self.array[index][1]

    def put(self, key, value):
        index = self._get_index(key)
        if index == -1:
            return

        if self.array[index]:
            self.array[index][1] = value
        else:
            self.array[index] = [key, value]
            self.count += 1

    def delete(self, key):
        index  = self._get_index(key)
        if index != -1 and self.array[index]:
            self.array[index] = []
            self.count -= 1

    def load_factor(self):
        return float(self.count)/self.capacity

if __name__ == '__main__':
    h = HashMap()
    h.put(123, 4)
    h.put('k1', 'v1')
    h.put('k1', 'v1_new')
    h.put('k2', 'v2')
    assert h.get('k1') == 'v1_new'
    assert h.get(123) == 4

    h.put('k3', 'v3')
    assert h.get('k3') == 'v3'

    h.delete('k4')

    h.delete('k3')
    assert not h.get('k3')

    print("load factor: ", h.load_factor())

    for i in range(512):
        h.put(i, i)

    print("load factor: ", h.load_factor())
    print(h.array)
