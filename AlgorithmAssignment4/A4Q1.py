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
    state = [(0, col, ld, rd)]
    while len(state) > 0:
        cur_state = state.pop()
        row = cur_state[0]
        column = cur_state[1]
        left_diagonal = cur_state[2]
        right_diagonal = cur_state[3]
        if row in placed_rows:
            state.append((row + 1, column, left_diagonal, right_diagonal))
        else:
            possible_column = ((1 << chessboard) - 1) & ~column & ~(left_diagonal >> row) & \
                              ~(right_diagonal >> (chessboard - 1 - row))
            while possible_column:
                cur_pos = possible_column & -possible_column
                if row < chessboard - 1:
                    state.append((row + 1, column ^ cur_pos, left_diagonal ^ (cur_pos << row), right_diagonal ^ (cur_pos << (chessboard - 1 - row))))
                else:
                    count += 1
                possible_column ^= cur_pos
    return count


num_case = int(sys.stdin.readline())
for _ in range(num_case):
    s = sys.stdin.readline().split()
    n, pos = len(s) // 2, []
    for i in range(n):
        pos.append((int(s[2*i]), int(s[2*i+1])))
    print(fourteen_queen(pos))
