N = int(input())  # N개의 재료
SB = [list(map(int, input().split())) for _ in range(N)]  # 신맛과 쓴맛 배열
min_v = 1e9  # 신맛과 쓴맛의 차이 최소값

def recur(cnt, sour, bitter):
    global min_v
    if cnt == N:
        min_v = min(min_v, abs(sour - bitter))
        return

    recur(cnt + 1, sour * SB[cnt][0], bitter + SB[cnt][1])  # 재료를 사용한 경우
    recur(cnt + 1, sour, bitter)  # 사용하지 않은 경우

for i in range(N):
    recur(i + 1, SB[i][0], SB[i][1])  # 적어도 하나 이상의 재료를 사용해야 함

print(min_v)