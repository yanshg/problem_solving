#!/usr/bin/python3

# Give 2 similar strings, efficiently list out all differences between them
#
# For example:
#  Input:  X = "XMJYAUZ",  Y = "XMJAZTZ"
#  Ouput:  X M J -Y A -U +A +T Z


# Idea:  First get longest common subsequence of the 2 strings,
#        then use the LCS to get diff-like output
#
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
#     DP[i][0] = 0     0<=i<=m
#     DP[0][j] = 0     0<=j<=n
#
# Results: DP[m][n] or DP[-1][-1]

def get_lcs_len(X, Y, m, n, DP):
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])

def get_diff(X, Y, m, n, DP):
    if m==0 and n==0:
        return

    if m==0 and n>0:
        print("+{}".format(Y[n-1:]), end=' ')
    elif n==0 and m>0:
        print("-{}".format(X[m-1:]), end=' ')
    elif X[m-1] == Y[n-1]:
        get_diff(X, Y, m-1, n-1, DP)
        print(X[m-1], end=" ")
    elif DP[m-1][n]>=DP[m][n-1]:
        get_diff(X, Y, m-1, n, DP)
        print("-{}".format(X[m-1]), end=' ')
    else:
        get_diff(X, Y, m, n-1, DP)
        print("+{}".format(Y[n-1]), end=' ')

def diff_utility(X, Y):
    print("X: ", X)
    print("Y: ", Y)
    m, n = len(X),len(Y)
    DP = [ [ 0 for j in range(n+1) ] for i in range(m+1) ]
    get_lcs_len(X, Y, m, n, DP)
    get_diff(X, Y, m, n, DP)
    print("\n")

#  Input:  X = "XMJYAUZ",  Y = "XMJAATZ"
#  Ouput:  X M J -Y A -U +A +T Z
diff_utility("XMJYAUZ", "XMJAZTZ")
