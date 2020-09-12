#!/usr/bin/python

# Article: Rabin-Karp algorithm to hash a string

import sys
if sys.version_info[0] == 3:
    _get_byte = lambda c: c
else:
    _get_byte = ord

def djb2_hash(data):
    assert isinstance(data, bytes)
    hash = 0
    for b in data:
        hash = hash * 26 + _get_byte(b)
    return hash

if __name__ == '__main__':
    keys = [ 'Hello', 'World', 'welcome', '123456', 123456 ]
    for key in keys:
        print(key, ": ", djb2_hash(str(key).encode('utf-8')))
