N, M = map(int, input().split())
answer = []

def dfs(cnt):
    if cnt == M:
        print(*answer)
        return

    for i in range(1, N+1):
        answer.append(i)
        dfs(cnt + 1)
        answer.pop()

dfs(0)