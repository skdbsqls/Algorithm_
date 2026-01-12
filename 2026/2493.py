N = int(input())
tops = list(map(int, input().split()))

ans = [0] * N
stack = []

for i in range(N-1, -1, -1):
    # stack의 마지막 놈의 길이보다 크거나 같은면
    while stack and tops[i] >= stack[-1][1]:
        ans[stack.pop()[0]] = i + 1  # 해당 탑의 인덱스에 수신한 탑의 인덱스 저장

    stack.append([i, tops[i]])  # [인덱스, 탑의 길이] 형태로 저장

print(*ans)
