import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 1

    # 가로 스도쿠 검증
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(arr[i][j])

        temp.sort()
        if nums != temp:
            result = 0
            break

    # 세로 스도쿠 검증
    for j in range(9):
        temp = []
        for i in range(9):
            temp.append(arr[i][j])

        temp.sort()
        if nums != temp:
            result = 0
            break

    # 3 * 3 스도쿠 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp = []
            for k in range(3):
                for h in range(3):
                    temp.append(arr[i + k][j + h])

            temp.sort()
            if nums != temp:
                result = 0
                break

    print(f'#{tc} {result}')