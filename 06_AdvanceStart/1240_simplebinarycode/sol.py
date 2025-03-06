import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 세로, 가로
    matrix = [list(map(int, input())) for _ in range(N)]  # 2차원 배열

    # 암호 코드 찾아내기
    code = []  # 암호 코드
    # 코드의 첫 비트는 0이 나올 가능성이 있으나, 마지막 비트는 무조건 1이므로 뒤에서부터 탐색
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if len(code) == 56:
                break
            if matrix[i][j] == 1:
                for k in range(56):
                    code.append(matrix[i][j - k])

    code.reverse()  # 배열 뒤집기

    # 암호코드 해독하기
    decode = []
    code_dict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }
    for i in range(0, len(code), 7):
        temp = ''
        for k in range(7):
            temp += str(code[i + k])
        decode.append(code_dict[temp])


    # 올바른 코드인지 알아내기
    odd = 0  # 홀수 자리의 합
    even = 0  # 짝수 자리의 합
    for i in range(8):
        if i % 2 == 0:
            odd += decode[i]
        else:
            even += decode[i]

    result = 0  # 결과
    if (odd * 3 + even) % 10 == 0:
        result = odd + even

    print(f'#{tc} {result}')
