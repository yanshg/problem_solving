#!/usr/bin/python

# Give 2 strings, print the longest common sequence of the 2 strings
#
# For example:
#  Input:  X = "XMJYAUZ",  Y = "MZJAWXU"
#  Ouput:  MJAU


# Use DP table
#
# DP[i][j]: the longest common sequence for X[:i+1] and Y[:j+1]
#
# X' = '' + X
# Y' = '' + Y
# lcs_str(X',Y') = lcs_str(X, Y)
#
# if X'[i] == Y'[j]:
#     DP[i][j] = DP[i-1][j-1] + X'[i]
# else:
#     DP[i][j] = max([DP[i-1][j], DP[[i][j-1]], key=len)
#
# ===>
#
# if X[i-1] == Y[j-1]:
#     DP[i][j] = DP[i-1][j-1] + X[i-1]
# else:
#     DP[i][j] = max([DP[i-1][j], DP[[i][j-1]], key=len)
#
# Base cases:
#     DP[i][0] = '' 0<=i<=m
#     DP[0][j] = '' 0<=j<=n
#
# Results: DP[m][n] or DP[-1][-1]

def get_lcs_str(X,Y):
    m, n = len(X),len(Y)
    DP = [ [ '' for j in range(n+1) ] for i in range(m+1) ]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                DP[i][j] = DP[i-1][j-1] + X[i-1]
            else:
                DP[i][j] = max([DP[i-1][j], DP[i][j-1]], key=len)

    return DP[-1][-1]

assert get_lcs_str("XMJYAUZ", "MZJAWXU") == "MJAU"
