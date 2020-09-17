#!/usr/bin/python

# Give one string, print the longest repeated subsequence of the string
#
# For example:
#  Input:  X = "ATACTCGGA"
#  Ouput:  ATCG


# Use DP table
#
# DP[i][j]: the longest repeating subsequence for X[:i+1] and X[:j+1]
#
# X' = '' + X
# lrs_str(X',X') = lrs_str(X, X)
#
# if X'[i] == X'[j] and i!=j:
#     DP[i][j] = DP[i-1][j-1] + X'[i]
# else:
#     DP[i][j] = max([DP[i-1][j], DP[[i][j-1]], key=len)
#
# ===>
#
# if X[i-1] == X[j-1]:
#     DP[i][j] = DP[i-1][j-1] + X[i-1]
# else:
#     DP[i][j] = max([DP[i-1][j], DP[[i][j-1]], key=len)
#
# Base cases:
#     DP[i][0] = '' 0<=i<=m
#     DP[0][j] = '' 0<=j<=n
#
# Results: DP[n][n] or DP[-1][-1]

def get_lrs_str(X):
    n = len(X)
    DP = [ [ '' for j in range(n+1) ] for i in range(n+1) ]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if X[i-1] == X[j-1] and i!=j:
                DP[i][j] = DP[i-1][j-1] + X[i-1]
            else:
                DP[i][j] = max([DP[i-1][j], DP[i][j-1]], key=len)

    return DP[-1][-1]

assert get_lrs_str("ATACTCGGA") == "ATCG"
