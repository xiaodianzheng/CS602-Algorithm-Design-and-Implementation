import sys


def fourteen_queen(pos):
    chessboard = 14
    count = 0
    col = 0
    ld = 0
    rd = 0
    for p in pos:
        col |= (1 << p[1] - 1)
        ld |= (1 << p[0] + p[1] - 2)
        rd |= (1 << chessboard - 1 - p[0] + p[1])
    placed_rows = set([p[0] - 1 for p in pos])

    def dfs(row, column, left_diagonal, right_diagonal):
        if row in placed_rows:
            dfs(row + 1, column, left_diagonal, right_diagonal)
        else:
            possible_column = ((1 << chessboard) - 1) & ~column & ~(left_diagonal >> row) & \
                              ~(right_diagonal >> (chessboard - 1 - row))
            while possible_column:
                cur = possible_column & -possible_column
                if row < chessboard - 1:
                    dfs(row + 1, column ^ cur, left_diagonal ^ (cur << row),
                        right_diagonal ^ (cur << (chessboard - 1 - row)))
                else:
                    nonlocal count
                    count += 1
                possible_column ^= cur

    dfs(0, col, ld, rd)
    return count


num_case = int(sys.stdin.readline())
for _ in range(num_case):
    s = sys.stdin.readline().split()
    n, pos = len(s) // 2, []
    for i in range(n):
        pos.append((int(s[2*i]), int(s[2*i+1])))
    print(fourteen_queen(pos))
