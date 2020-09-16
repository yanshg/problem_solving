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
    substr = ''
    DP = [ [''] * (n+1) for i in range(m+1) ]
    for i in range(1,m+1):
        for j in range(1,n+1):
            DP[i][j] = ''
            if X[i-1] == Y[j-1]:
                DP[i][j] = DP[i-1][j-1] + X[i-1]
                l = len(DP[i][j])
                if l > max_len:
                    max_len = l
                    substr = DP[i][j]
    return substr

assert get_lcs_substring('ABABC','BABCA') == 'BABC'

