#!/usr/bin/python

# Longest common substring of 2 strings.
#
# For example: 'ABABC' 'BABCA' has longest common substring 'BABC'
#

# use DP table
#
# DP[i][j]:  longest suffix string of X[:i+1] and Y[:j+1]
#
# X' = '' + X
# Y' = '' + Y
#
#            | 0                  if i==0 or j==0
# DP[i][j] = | 0                  if X[i-1]!=Y[j-1]
#            | DP[i-1][j-1] + 1   if X[i-1]==Y[j-1]

def get_lcs_substring(X, Y):
    m,n = len(X),len(Y)
    max_len = 0
    ending_index = 0
    DP = [ [0] * (n+1) for i in range(m+1) ]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
                if DP[i][j] > max_len:
                    max_len = DP[i][j]
                    ending_index = j

    return Y[ending_index-max_len:ending_index]

# Simplified to one dimension array
def get_lcs_substring2(X, Y):
    m,n = len(X),len(Y)
    max_len = 0
    ending_index = 0
    DP = [0] * (n+1)
    for i in range(1,m+1):
        for j in range(n,0,-1):
            if X[i-1] == Y[j-1]:
                DP[j] = DP[j-1] + 1
                if DP[j] > max_len:
                    max_len = DP[j]
                    ending_index = j

    return Y[ending_index-max_len:ending_index]

assert get_lcs_substring('ABABC','BABCA') == 'BABC'
assert get_lcs_substring2('ABABC','BABCA') == 'BABC'

