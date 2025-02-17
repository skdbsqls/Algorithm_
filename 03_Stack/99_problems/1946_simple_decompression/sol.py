import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    CiKi = [input().split() for _ in range(N)]

    result = []  # 최종
    temp = []  # 10개짜리
    for CK in CiKi:
        ci = CK[0]
        ki = int(CK[1])

        # 연속된 개수가 0이 될 때까지
        while ki > 0:
            # 길이가 10이 되면
            if len(temp) == 10:
                # result에 push하고, temp는 다시 비우기
                result.append(temp)
                temp = []

            # temp에 알파벳 넣고, 연속된 개수 - 1
            temp.append(ci)
            ki -= 1

        # 마지막 압축인 경우, 남은 문서 push 해주기
        if CK == CiKi[-1]:
            result.append(temp)

    # 출력
    print(f'#{tc}')
    for i in range(len(result)):
        print(f'{"".join(result[i])}')