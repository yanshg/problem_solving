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

import sys

if sys.version_info[0] == 3:
    _get_byte = lambda c:c
else:
    _get_byte = ord

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
        string = ''
        node = self.head
        while node:
            string += '[{}, {}] '.format(node.key, node.value)
            node = node.next

        return string

    def is_empty(self):
        return self.head == self_tail

    def append(self, node):
        if self.tail:
            node.prev = self.tail
            node.next = None
            self.tail.next = node

        self.tail = node

        if not self.head:
            self.head = node

    def delete(self, node):
        prev = node.prev
        next = node.next

        if not prev:
            prev.next = next

        if not next:
            next.prev = prev

        if self.head == node:
            self.head = next

        if self.tail == node:
            self.tail = prev

    def popleft(self):
        if not self.head:
            return

        head = self.head
        self.head = head.next
        self.head.prev = None

        return head

    def get_node(self, key):
        node = self.head
        while node and node.key != key:
            node = node.next

        return node

class HashMap:
    def __init__(self,capacity=CAPACITY):
        self.capacity = capacity
        self.array = [ 0 for i in range(capacity) ]

    # DJB2 Hash algorithm
    def _hash(self, key):
        bs = str(key).encode('utf-8')
        hash =  5381
        for b in bs:
            hash = (hash * 33) + _get_byte(b)
        return hash % len(self.array)

    # return (index for the exist key, index which available for the key, Node pointer)
    def _get_index(self, key):
        index = self._hash(key)
        if not self.array[index]:
            return (-1, index, None)

        node = self.array[index].get_node(key)
        if node:
            return (index, index, node)

        return (-1, index, None)

    def exists(self, key):
        exist_index,_,_ = self._get_index(key)
        return exist_index != -1

    def get(self, key):
        exist_index,_,node  = self._get_index(key)
        if exist_index == -1 or not node:
            return None

        return node.value

    def put(self, key, value):
        exist_index,avail_index,node = self._get_index(key)
        if exist_index != -1 and node:
            node.value = value
            return

        self.array[avail_index] = DoubleLinkedList()
        self.array[avail_index].append(Node(key, value))

    def delete(self, key):
        exist_index,_,node  = self._get_index(key)
        if exist_index != -1 and node:
            self.array[exist_index].delete(node)

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

    #h.delete('k4')

    #h.delete('k3')
    #assert not h.get('k3')

    for i in range(512):
        h.put(i, i)

    print(h.array)
