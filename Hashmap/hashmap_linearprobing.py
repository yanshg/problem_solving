#!/usr/bin/python

# Hashmap with fixed size and linear probing
#
# Along with quadratic probing and double hashing,
# linear probing is a form of open addressing.
#
# Article: https://en.wikipedia.org/wiki/Linear_probing
#
# 1. Each cell of a hash table stores a single key-value pair.
# 2. When the hash function causes a collision by mapping a new key to a cell of the hash table that is already occupied by another key, linear probing searches the table for the closest following free location and inserts the new key there.
# 3. Lookups are performed in the same way, by searching the table sequentially starting at the position given by the hash function, until finding a cell with a matching key or an empty cell.

CAPACITY = 256

LINEAR_PROBING=0
DOUBLE_HASH=2

class HashMap:
    def __init__(self,capacity=CAPACITY,probe_mode=LINEAR_PROBING):
        self.capacity = capacity
        self.array = [ [] for i in range(capacity) ]
        self.probe_mode = probe_mode

    # DJB2 Hash algorithm
    def _hash(self, key):
        bs = str(key).encode('utf-8')
        hash =  5381
        for b in bs:
            hash = (hash * 33) + b
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

            index = (index + 1) % len(self.array)
            if index == orig_index:
                return (-1, -1)

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

    def delete(self, key):
        exist_index,_  = self._get_index(key)
        if exist_index != -1:
            self.array[exist_index] = []

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

    for i in range(512):
        h.put(i, i)

    print(h.array)
