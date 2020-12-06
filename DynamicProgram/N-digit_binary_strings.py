#!/usr/bin/python

'''

Find all N-digit binary strings without any consecutive 1's

For example, for N = 5 the binary strings satisfies the given constraints are

00000
00001
00010
00100
00101
01000
01001
01010
10000
10001
10010
10100
10101

total 13 strings.

'''

# use DP table
#
# DP[i][0]: means counts of N-binary string which i-th digit is 0
# DP[i][0]: means counts of N-binary string which i-th digit is 1
#
# Base cases:
#       DP[n-1][0] = 1
#       DP[n-1][1] = 1
#
# Result:   DP[0][0] + DP[0][1]

def countStrings(n):
    DP = [ [1,1] for i in range(n) ]
    for i in range(n-2,-1,-1):
        DP[i][0] = DP[i+1][0] + DP[i+1][1]
        DP[i][1] = DP[i+1][0]

    return DP[0][0] + DP[0][1]

def get_all_strings(n):
    DP = [ [[],[]] for i in range(n) ]
    DP[-1]=[['0'],['1']]

    for i in range(n-2,-1,-1):
        DP[i][0] = [ '0'+item for item in DP[i+1][0] + DP[i+1][1] ]
        DP[i][1] = [ '1'+item for item in DP[i+1][0] ]

    result = DP[0][0] + DP[0][1]
    #print(result)
    return result

assert countStrings(5) == 13
assert get_all_strings(5) = ['00000', '00001', '00010', '00100', '00101', '01000', '01001', '01010', '10000', '10001', '10010', '10100', '10101']
