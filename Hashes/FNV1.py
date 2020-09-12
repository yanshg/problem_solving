#!/usr/bin/python

# Article:
#   https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
#   http://www.isthe.com/chongo/tech/comp/fnv/index.html

# FNV1/FNV1a hash algorithm

FNV_PRIME_32=0x01000193
FNV_OFFSET_BASIS_32=0x811c9dc5
FNV_PRIME_64=0x00000100000001b3
FNV_OFFSET_BASIS_64=0xcbf29ce484222325

import sys

if sys.version_info[0]==3:
    _get_byte=lambda c:c
else:
    _get_byte=ord

def fnv1(data,fnv_prime,fnv_offset_basis):
    assert isinstance(data, bytes)
    hash = fnv_offset_basis
    for b in data:
        hash = (hash * fnv_prime) ^ _get_byte(b)
    return hash

def fnv1a(data,fnv_prime,fnv_offset_basis):
    assert isinstance(data, bytes)
    hash = fnv_offset_basis
    for b in data:
        hash = (hash ^ _get_byte(b)) * fnv_prime
    return hash

def fnv1_32(data):
    return fnv1(data, FNV_PRIME_32, FNV_OFFSET_BASIS_32)

def fnv1a_32(data):
    return fnv1a(data, FNV_PRIME_32, FNV_OFFSET_BASIS_32)

def fnv1_64(data):
    return fnv1(data, FNV_PRIME_64, FNV_OFFSET_BASIS_64)

def fnv1a_64(data):
    return fnv1a(data, FNV_PRIME_64, FNV_OFFSET_BASIS_64)


if __name__ == '__main__':
    keys = [ 'Hello', 'World', 'welcome', '21323', 21323 ]
    for key in keys:
        print(key, ": ", fnv1a_32(str(key).encode('utf-8')))
