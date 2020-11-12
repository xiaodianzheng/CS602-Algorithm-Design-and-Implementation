import sys


def calculate_row(pos):
    row = 0
    for p in pos:
        row |= (1 << 14 - p[1])
    return row


def calculate_ld(pos):
    ld = [0 for _ in range(14)]
    for i in range(14):
        for p in pos:
            cur_ld = 15 - p[1] - p[0] + i
            if cur_ld < 0 or cur_ld > 13:
                continue
            else:
                ld[i] |= (1 << 15 - p[1] - p[0] + i)
    return ld


def calculate_rd(pos):
    rd = [0 for _ in range(14)]
    for i in range(14):
        for p in pos:
            cur_ld = 13 - p[1] + p[0] - i
            if cur_ld < 0 or cur_ld > 13:
                continue
            else:
                rd[i] |= (1 << 13 - p[1] + p[0] - i)
    return rd


def fourteen_queen(pos):
    count = 0
    row = calculate_row(pos)
    all_ld = calculate_ld(pos)
    all_rd = calculate_rd(pos)
    target = (1 << 14) - 1
    placed_rows = set([p[0] - 1 for p in pos])

    def dfs_bitwise(row, ld, rd, cur_rows):
        nonlocal count
        if cur_rows in placed_rows:
            p = 0
            # ld = ld | all_ld[cur_rows]
            # rd = rd | all_rd[cur_rows]
            dfs_bitwise(row + p, (ld + p) << 1, (rd + p) >> 1, cur_rows + 1)
        elif row != target:
            ld = ld | all_ld[cur_rows]
            rd = rd | all_rd[cur_rows]
            valid_rows = target & ~(row | ld | rd)
            while valid_rows != 0:
                p = valid_rows & -valid_rows
                valid_rows = valid_rows - p
                dfs_bitwise(row + p, (ld + p) << 1, (rd + p) >> 1, cur_rows + 1)
        else:
            count += 1

    dfs_bitwise(row, 0, 0, 0)
    return count


num_case = int(sys.stdin.readline())
for _ in range(num_case):
    s = sys.stdin.readline().split()
    n, pos = len(s) // 2, []
    for i in range(n):
        pos.append((int(s[2*i]), int(s[2*i+1])))
    print(fourteen_queen(pos))
