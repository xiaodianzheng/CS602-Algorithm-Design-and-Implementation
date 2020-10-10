import sys

def driving_mode(batt, num_seg, data):
    return 0.0

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    batt, num_seg = float(s[0]) / 100, int(s[1])
    data = []
    for i in range(num_seg):
        data.append([float(t) for t in s[i+2].split(':')])
    print('%.2f' % driving_mode(batt, num_seg, data))
