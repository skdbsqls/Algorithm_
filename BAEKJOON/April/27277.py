N = int(input())
abilities = list(map(int, input().split()))

abilities = sorted(abilities)
ans = 0
if N % 2 == 0:
    for i in range(0, N // 2 - 1):
        temp = abilities[-(i + 1)] - abilities[i]
        ans += temp
else:
    for i in range(0, N // 2):
        temp = temp = abilities[-(i + 1)] - abilities[i]
        ans += temp

ans += abilities[N // 2]

print(ans)