#!/usr/bin/python

# Seperate chaining with linked list
#
# 1. Require only basic data structures with simple algorithms,
# 2. Can use simple hash functions that are unsuitable for other methods
# 3. Remain effective even when the number of table entries n is much higher than the number of buckets.

# For separate-chaining, the worst-case scenario is when all entries are inserted into the same bucket,
#
# The bucket chains are often searched sequentially using the order the entries were added to the bucket.
# so usually when the entries exceed 8, then use balanced binary search tree, like red-black tree to
#
# Disadvantages:
#
# 1. When storing small keys and values, the space overhead of the next pointer in each entry record can be significant.
# 2. Traversing a linked list has poor cache performance, making the processor cache ineffective.

CAPACITY = 512

import hashlib

class Node:
    def __init__(self,key,value,prev=None,next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        string = '#'
        while node:
            #string += '[{}, {}] '.format(node.key, node.value)
            string += '{},'.format(node.key)
            node = node.next
        string += '#'

        return string

    def append(self, node):
        if self.head is None and self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

    def delete(self, node):
        if not node:
            return

        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev

        if self.head == node:
            self.head = next
        if self.tail == node:
            self.tail = prev

    def get_node(self, key):
        node = self.head
        while node and node.key != key:
            node = node.next
        return node

class HashMap:
    def __init__(self,capacity=CAPACITY):
        self.capacity = capacity
        self.array = [ 0 for i in range(capacity) ]
        self.count = 0

    def _hash(self, key):
        hash = int(hashlib.sha1(str(key).encode('utf-8')).hexdigest(), 16)
        return hash % len(self.array)

    # return (index for the exist key, index which available for the key, Node pointer)
    def _get_index_node(self, key):
        index = self._hash(key)
        linkedlist = self.array[index]
        node = linkedlist.get_node(key) if linkedlist else None
        return (index, node)

    def exists(self, key):
        index,node = self._get_index_node(key)
        return bool(node)

    def get(self, key):
        index,node = self._get_index_node(key)
        return node.value if node else None

    def put(self, key, value):
        index,node = self._get_index_node(key)
        if node:
            node.value = value
            return

        if not self.array[index]:
            self.array[index] = DoubleLinkedList()

        self.array[index].append(Node(key, value))
        self.count += 1

    def delete(self, key):
        index,node = self._get_index_node(key)
        if node:
            self.array[index].delete(node)
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
    #assert not h.get('k3')

    for i in range(1512):
        h.put(i, i)

    print(h.array)

    print("load factor: ", h.load_factor())
