import sys
import copy


def move(initial, a, b, c, flag1, flag2, count):
    '''
    The time complexity is O(n)
    '''
    if b == [] and c == []:
        return count
    elif a == [] and c == []:
        return count
    elif a == [] and b == []:
        return count
    elif a == initial[0] and b == initial[1] and c == initial[2] and count != 0:
        return float("inf")
    elif len(a) > 1:
        for i in range(0, len(a) - 1):
            if (a[i] + a[i + 1]) % 2 == 0:
                return float("inf")
    elif len(b) > 1:
        for i in range(0, len(b) - 1):
            if (b[i] + b[i + 1]) % 2 == 0:
                return float("inf")
    elif len(c) > 1:
        for i in range(0, len(c) - 1):
            if (c[i] + c[i + 1]) % 2 == 0:
                return float("inf")
    # odd
    if flag1:
        if a and a[0] == 1:
            if len(a) == 1:
                b.insert(0, a.pop(0)) if flag2 else c.insert(0, a.pop(0))
                count += 1
            else:
                size = 1
                for i in range(1, len(a)):
                    if a[i] == a[i - 1] + 1:
                        size += 1
                    else:
                        break
                if size % 2 == 0:
                    if flag2:
                        c = a[:size] + c
                    else:
                        b = a[:size] + b

                    for i in range(size):
                        a.pop(0)
                else:
                    if flag2:
                        b = a[:size] + b
                    else:
                        c = a[:size] + c
                    for i in range(size):
                        a.pop(0)
                count += 2 ** size - 1
        elif b and b[0] == 1:
            if len(b) == 1:
                c.insert(0, b.pop(0)) if flag2 else a.insert(0, b.pop(0))
                count += 1
            else:
                size = 1
                for i in range(1, len(b)):
                    if b[i] == b[i - 1] + 1:
                        size += 1
                    else:
                        break
                if size % 2 == 0:
                    if flag2:
                        a = b[:size] + a
                    else:
                        c = b[:size] + c
                    for i in range(0, size):
                        b.pop(0)
                else:
                    if flag2:
                        c = b[:size] + c
                    else:
                        a = b[:size] + a
                    for i in range(0, size):
                        b.pop(0)
                count += 2 ** size - 1
        elif c and c[0] == 1:
            if len(c) == 1:
                a.insert(0, c.pop(0)) if flag2 else b.insert(0, c.pop(0))
                count += 1
            else:
                size = 1
                for i in range(1, len(c)):
                    if c[i] == c[i - 1] + 1:
                        size += 1
                    else:
                        break
                if size % 2 == 0:
                    if flag2:
                        b = c[:size] + b
                    else:
                        a = c[:size] + a
                    for i in range(0, size):
                        c.pop(0)
                else:
                    if flag2:
                        a = c[:size] + a
                    else:
                        b = c[:size] + b
                    for i in range(0, size):
                        c.pop(0)
                count += 2 ** size - 1
    # even
    else:
        count += 1
        if a and a[0] == 1:
            if not b:
                b.insert(0, c.pop(0))
            elif not c:
                c.insert(0, b.pop(0))
            elif b[0] > c[0]:
                b.insert(0, c.pop(0))
            elif b[0] < c[0]:
                c.insert(0, b.pop(0))
        elif b and b[0] == 1:
            if not a:
                a.insert(0, c.pop(0))
            elif not c:
                c.insert(0, a.pop(0))
            elif a[0] > c[0]:
                a.insert(0, c.pop(0))
            elif a[0] < c[0]:
                c.insert(0, a.pop(0))
        elif c and c[0] == 1:
            if not a:
                a.insert(0, b.pop(0))
            elif not b:
                b.insert(0, a.pop(0))
            elif a[0] > b[0]:
                a.insert(0, b.pop(0))
            elif a[0] < b[0]:
                b.insert(0, a.pop(0))
    return move(initial, a, b, c, not flag1, flag2, count)


def tower_hanoi(disk):
    counts = []
    options = ["odd clockwise", "odd counterclockwise", "even clockwise", "even counterclockwise"]

    n = len(disk[0]) + len(disk[1]) + len(disk[2])
    if disk[0] != [] and disk[0][-1] == n:
        peg = 'A'
    elif disk[1] != [] and disk[1][-1] == n:
        peg = 'B'
    elif disk[2] != [] and disk[2][-1] == n:
        peg = 'C'

    for i in range(0,3):
        if len(disk[i]) > 1:
            for j in range(0, len(disk[i]) - 1):
                if (disk[i][j] + disk[i][j + 1]) % 2 == 0:
                    print("impossible")
                    return

    initial = copy.deepcopy(disk)

    count = move(initial, disk[0], disk[1], disk[2], True, True, 0)
    counts.append(count)

    disk = copy.deepcopy(initial)
    count = move(initial, disk[0], disk[1], disk[2], True, False, 0)
    counts.append(count)

    disk = copy.deepcopy(initial)
    count = move(initial, disk[0], disk[1], disk[2], False, True, 0)
    counts.append(count)

    disk = copy.deepcopy(initial)
    count = move(initial, disk[0], disk[1], disk[2], False, False, 0)
    counts.append(count)

    index = counts.index(min(counts))
    if counts == [float('inf')] * 4:
        print("impossible")
    elif min(counts) == 0:
        print(peg, counts[index])
    else:
        print(peg, counts[index], options[index])


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    disk = [[int(t) for t in s.split()] for s in sys.stdin.readline().split(',')]
    tower_hanoi(disk)
