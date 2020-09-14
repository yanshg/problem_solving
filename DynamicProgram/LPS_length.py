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

def get_lps_len(X):
    n = len(X)
    DP = [ [ 0 for j in range(n) ] for i in range(n) ]
    for i in range(n):
        DP[i][i] = 1

    for c in range(1, n):
        for i in range(n-c):
            j = i + c
            if X[i] == X[j]:
                DP[i][j] = DP[i+1][j-1] + 2
            else:
                DP[i][j] = max(DP[i+1][j], DP[i][j-1])

    return DP[0][-1]

# Simplify to use one dimension array. O(N^2), space(O(2*N))
def get_lps_len2(X):
    n = len(X)
    DP_last = [0] * (n-1)
    DP = [1] * n

    for c in range(1,n):
        for i in range(n-c):
            j = i + c
            if X[i] == X[j]:
                DP[i] = DP_last[i] + 2
            else:
                DP[i] = max(DP[i], DP[i+1])
            DP_last[i] = DP[i+1]
        print("DP_last:", DP_last[:(n-c-1)])
        print("DP:", DP[:(n-c)])

    return DP[0]

assert get_lps_len("ABBDCACB") == 5
assert get_lps_len2("ABBDCACB") == 5
