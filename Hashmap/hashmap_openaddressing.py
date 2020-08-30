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

import sys,hashlib

if sys.version_info[0] == 3:
    _get_byte = lambda c:c
else:
    _get_byte = ord

class HashMap:
    def __init__(self,capacity=CAPACITY,probe_mode=LINEAR_PROBING):
        self.capacity = capacity
        self.array = [ [] for i in range(capacity) ]
        self.probe_mode = probe_mode
        self.count = 0

    # DJB2 Hash algorithm
    def _hash(self, key):
        bs = str(key).encode('utf-8')

        use_simple_hash_function = False
        if use_simple_hash_function:
            hash =  5381
            for b in bs:
                hash = (hash * 33) + _get_byte(b)
        else:
            hash = int(hashlib.md5(bs).hexdigest(), 16)
        return hash % len(self.array)

    # return (index for the exist key, index which available for the key)
    def _get_index(self, key):
        index = self._hash(key)
        orig_index = index
        while True:
            if not self.array[index]:
                return (-1, index)

            if self.array[index][0] == key:
                return (index, index)

            # Linear probing
            index = (index + 1) % len(self.array)
            if index == orig_index:
                break

        return (-1, -1)

    def exists(self, key):
        exist_index,_ = self._get_index(key)
        return exist_index != -1

    def get(self, key):
        exist_index,_  = self._get_index(key)
        if exist_index == -1:
            return None

        return self.array[exist_index][1]

    def put(self, key, value):
        exist_index,avail_index = self._get_index(key)
        if exist_index != -1:
            self.array[exist_index][1] = value
        elif avail_index != -1:
            self.array[avail_index] = [key, value]
            self.count += 1

    def delete(self, key):
        exist_index,_  = self._get_index(key)
        if exist_index != -1:
            self.array[exist_index] = []
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
