import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    CiKi = [input().split() for _ in range(N)]

    result = []
    temp = []
    for CK in CiKi:
        ci = CK[0]
        ki = int(CK[1])

        while ki > 0:
            if len(temp) == 10:
                result.append(temp)
                temp = []

            temp.append(ci)
            ki -= 1

        if CK == CiKi[-1]:
            result.append(temp)

    # 출력
    print(f'#{tc}')
    for i in range(len(result)):
        print(f'{"".join(result[i])}')