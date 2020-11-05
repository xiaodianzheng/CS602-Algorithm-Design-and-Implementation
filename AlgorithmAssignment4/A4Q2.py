import sys

def escape(n, roadmap, qrtn, spaceship):
    return [0] * n

n = int(sys.stdin.readline())
roadmap = {}
s = sys.stdin.readline().split()
for t in s:
    u = t.split(':')
    roadmap[int(u[0]), int(u[1])] = int(u[2])
qrtn = [0] * (n + 1)
s = sys.stdin.readline().split()
i = 1
for t in s:
    u = t.split(':')
    qrtn[i] = int(u[0]), int(u[1])
    i += 1
spaceship = [int(t) for t in sys.stdin.readline().split()]
print(' '.join([str(i) for i in escape(n, roadmap, qrtn, spaceship)]))
