import sys


def get_lcs(a, b, i, j):
    """
    The time complexity of this function is O(mn) where m is the length of a and n is the length of b
    """
    mat = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                mat[i][j] = mat[i - 1][j - 1] + 1
            else:
                mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])

    lcs = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs.append(a[i - 1])
            i -= 1
            j -= 1
        elif mat[i - 1][j] >= mat[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs[::-1]


def LCMS(a, b):
    """
    The total time complexity is O(mn) where m is the length of a and n is the length of b
    """
    new_a = []
    new_b = []
    for ai in a:
        new_a.append(int(ai, 16))
    for bi in b:
        new_b.append(int(bi, 16))

    lcs = get_lcs(new_a, new_b, len(new_a), len(new_b))
    up = [1 for _ in lcs]
    down = [1 for _ in lcs]
    for i in range(1, len(lcs)):
        for j in range(0, i):
            if lcs[i] > lcs[j] and up[i] < up[j] + 1:
                up[i] = up[j] + 1
    for i in range(len(lcs) - 2, -1, -1):
        for j in range(len(lcs) - 1, i, -1):
            if lcs[i] > lcs[j] and down[i] < down[j] + 1:
                down[i] = down[j] + 1
    res = 0
    for i in range(0, len(lcs)):
        res = max(res, up[i] + down[i] - 1)
    return res


num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    a = sys.stdin.readline().split()
    b = sys.stdin.readline().split()
    print(LCMS(a, b))
