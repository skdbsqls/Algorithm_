"1072 게임"

import sys, math
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = (100 * Y) // X

if Z >= 99:
    print(-1)
else:
    # n은 조건을 만족하는 가장 작은 정수가 되어야 함으로 올림해야만
    ans = math.ceil(((Z + 1) * X - 100 * Y) / (99 - Z))
    print(ans)
