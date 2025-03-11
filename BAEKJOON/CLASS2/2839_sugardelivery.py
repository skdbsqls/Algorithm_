N = int(input())

cnt = 0
while N % 5 != 0 and N > 2:
    N -= 3
    cnt += 1

while N > 4:
    N -= 5
    cnt += 1

if 0 < N < 3:
    print(-1)
else:
    print(cnt)