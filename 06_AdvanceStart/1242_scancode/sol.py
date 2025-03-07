import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 세로, 가로
    matrix = [input() for _ in range(N)]

    # 해독할 16진수 코드 찾기
    code = ''
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != '0':
                code += matrix[i][j]
        if code:
            break

    # 16진수를 2진수로 바꾸기
    code = int(code, 16)  # 16진수를 10진수로
    code = bin(code)  # 10진수를 2진수로 -> 0b(이진수)

    print(code)