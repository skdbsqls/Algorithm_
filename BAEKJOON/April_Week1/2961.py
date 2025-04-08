N = int(input())  # N개의 재료
SB = [list(map(int, input().split())) for _ in range(N)]

# 신맛의 곱 계산하기
def cal_S(cnt, total):
    if cnt == N:
        print(total)
        return

    cal_S(cnt + 1, total * SB[cnt][0])  # 포함 하는 경우
    cal_S(cnt + 1, total)  # 포함 안 하는 경우

# 쓴맛의 합 계산하기
def cal_B(cnt, total):
    if cnt == N:
        print(total)
        return

    cal_B(cnt + 1, total + SB[cnt][1])
    cal_B(cnt + 1, total)