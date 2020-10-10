import sys

def LCMS(a, b):
    return abs(len(a) - len(b)) + 2

num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    a = sys.stdin.readline().split()
    b = sys.stdin.readline().split()
    print(LCMS(a, b))
