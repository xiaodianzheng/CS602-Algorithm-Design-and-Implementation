import sys


def LCMS(a, b):
    """
    The worst case time complexity is O(n^2) where n is min(len(A), len(B)) when A and B are identical.
    """
    common_sequence = []
    for n in a:
        if n in b:
            common_sequence.append(int(n, 16))
            b = b[b.index(n) + 1:]
    n = len(common_sequence)
    increase_indexes = [1] * n
    decrease_indexes = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if common_sequence[i] > common_sequence[j] \
                    and increase_indexes[i] < increase_indexes[j] + 1:
                increase_indexes[i] = increase_indexes[j] + 1
    for i in range(n-2, -1, -1):
        for j in range(i-1, n):
            if common_sequence[i] > common_sequence[j] \
                    and decrease_indexes[i] < decrease_indexes[j] + 1:
                decrease_indexes[i] = decrease_indexes[j] + 1
    res = 0
    for i in range(1, n):
        res = max(res, increase_indexes[i] + decrease_indexes[i] - 1)
    return res


num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    a = sys.stdin.readline().split()
    b = sys.stdin.readline().split()
    print(LCMS(a, b))
