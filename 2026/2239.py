"2239 스도쿠"

import sys
input = sys.stdin.readline

board = [list(map(int, input().strip())) for _ in range(9)]

# 숫자 사용 여부 체크
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
box = [[False] * 10 for _ in range(9)]

# 처음 상태 반영
for i in range(9):
    for j in range(9):
        n = board[i][j]

        if n != 0:
            row[i][n] = True
            col[j][n] = True
            b = (i // 3) * 3 + (j // 3)
            box[b][n] = True

def dfs(cnt):
    # 종료 조건
    if cnt == 81:
        for i in range(9):
            print(''.join(map(str, board[i])))
        sys.exit(0) # 강제 종료

    i = cnt // 9
    j = cnt % 9

    # 이미 채워진 칸이면
    if board[i][j] != 0:
        dfs(cnt + 1)
    # 그렇지 않으면
    else:
        b = (i // 3) * 3 + (j // 3)

        # 1부터 9까지 넣을 수 있는지 시도
        for num in range(1, 10):
            # 해당 숫자를 넣을 수 있으면
            if not row[i][num] and not col[j][num] and not box[b][num]:
                board[i][j] = num
                row[i][num] = True
                col[j][num] = True
                box[b][num] = True

                dfs(cnt + 1)

                # 백트레킹(원복)
                board[i][j] = 0
                row[i][num] = False
                col[j][num] = False
                box[b][num] = False

dfs(0)