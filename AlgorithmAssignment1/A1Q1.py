import sys

def power_modulo(m, k, n):
    '''
    The time complexity is O(logk)
    '''
    res = 1
    m = m % n
    if k == 0:
        return res
    res = power_modulo(m ** 2 % n, k // 2, n)
    if k % 2 == 1:
        res = res * m % n
    return res

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    print(power_modulo(m, k, n))
