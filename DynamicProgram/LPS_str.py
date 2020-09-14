#!/usr/bin/python

# Give one string, print the longest palindromic subsequence of the string
#
# For example:
#  Input:  X = "ABBDCACB"
#  Ouput:  5 (BCACB)


# Use DP table
#
# DP[i][j]: the length of longest palindromic subsequence for X[i:j+1]
#
#            |  0                              if i>j
#            |  1                              if i==j
# DP[i][j] = |  DP[i+1][j-1]+2                 if X[i] == X[j]
#            |  max(DP[i+1][j], DP[[i][j-1])   if X[i]!=X[j]
#
# Results: DP[0][n-1]

def get_lps_str(X):
    n = len(X)
    DP = [ [ '' for j in range(n) ] for i in range(n) ]
    for i in range(n):
        DP[i][i] = X[i]

    for c in range(1, n):
        for i in range(n-c):
            j = i + c
            if X[i] == X[j]:
                DP[i][j] = X[i] + DP[i+1][j-1] + X[j]
            else:
                DP[i][j] = max([DP[i+1][j], DP[i][j-1]], key=len)

    return DP[0][-1]

assert get_lps_str("ABBDCACB") == 'BCACB'
