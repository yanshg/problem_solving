#!/usr/bin/python

# Give 2 strings, print the longest common sequence of the 2 strings
#
# For example:
#  Input:  X = "ABCBDAB",  Y = "BDCABA"
#  Ouput:  BCAB, BCBA, BDAB


# Use DP table
#
# DP[i][j]: the length of longest common sequence for X[:i+1] and Y[:j+1]
#
# X' = '' + X
# Y' = '' + Y
# lcs_len(X',Y') = lcs_len(X, Y)
#
# if X'[i] == Y'[j]:
#     DP[i][j] = DP[i-1][j-1] + 1
# else:
#     DP[i][j] = max(DP[i-1][j], DP[[i][j-1])
#
# ===>
#
# if X[i-1] == Y[j-1]:
#     DP[i][j] = DP[i-1][j-1] + 1
# else:
#     DP[i][j] = max(DP[i-1][j], DP[[i][j-1])
#
# Base cases:
#     DP[i][0] = 0    0<=i<=m
#     DP[0][j] = 0    0<=j<=n
#
# Results: DP[m][n] or DP[-1][-1]

def get_lcs_length(X, Y, m, n, DP):
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])

    return DP

def get_all_lcs_subseqs(X, Y, m, n, DP):
    if m==0 or n==0:
        return [ '' ]

    if X[m-1] == Y[n-1]:
        # get lcs strings of left top
        lcs = get_all_lcs_subseqs(X, Y, m-1, n-1, DP)
        return [ x + X[m-1] for x in lcs ]

    # if top > left
    if DP[m-1][n] > DP[m][n-1]:
        # get lcs strings of top
        return get_all_lcs_subseqs(X, Y, m-1, n, DP)

    # if left > top
    if DP[m-1][n] < DP[m][n-1]:
        # get lcs strings of left
        return get_all_lcs_subseqs(X, Y, m, n-1, DP)

    # if top == left, get lcs strings of both top and left
    top = get_all_lcs_subseqs(X, Y, m-1, n, DP)
    left = get_all_lcs_subseqs(X, Y, m, n-1, DP)
    return top + left

def get_lcs_allsubseqs(X,Y):
    m, n = len(X),len(Y)
    DP = [ [ 0 for j in range(n+1) ] for i in range(m+1) ]

    get_lcs_length(X, Y, m, n, DP)
    return set(get_all_lcs_subseqs(X, Y, m, n, DP))


assert get_lcs_allsubseqs("ABCBDAB", "BDCABA") == { 'BCAB', 'BCBA', 'BDAB' }
