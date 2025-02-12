import sys

sys.stdin = open('sample_input.txt')

# 풀이 1
T = int(input())
for tc in range(1, T + 1):
    board = [list(input()) for _ in range(5)]

    # 가장 긴 행의 길이 구하기
    max_len = len(board[0])
    for i in range(5):
        if max_len < len(board[i]):
            max_len = len(board[i])

    # 가장 긴 행의 길이 * 5 만큼의 2차원 배열 생성하기
    arr = [[0] * max_len for _ in range(5)]

    # 2차원 배열에 알맞은 위치에 글자 넣어주기
    for i in range(5):
        for j in range(len(board[i])):
            arr[i][j] = board[i][j]

    # 0이 아닌 글자가 있다면, 열 우선 순회로 결과에 담아주기
    result = ''
    for j in range(max_len):
        for i in range(5):
            if arr[i][j] != 0:
                result += arr[i][j]

    print(f'#{tc} {result}')

# 풀이 2
T = int(input())
for tc in range(1, T + 1):
    board = [list(input()) for _ in range(5)]

    # 가장 긴 행의 길이 구하기
    max_row = 0
    for row in board:
        max_row = max(max_row, len(row))

    letters = []

    # 세로로 순회
    for i in range(max_row):  # 가장 긴 행의 길이만큼 반복
        for j in range(5):  # 안쪽은 5번만 반복
            # j번째 줄이 현재 확인하고 있는 i보다 길다는 것을 확인
            if len(board[j]) <= i:
                # 작거나 같으면 나머지는 실행 안 함
                continue
            # 글자를 추가해준다.
            letters.append(board[j][i])  # 먼저 바뀌는 쪽이 앞에 옴

    print(f'#{tc} {"".join(letters)}')