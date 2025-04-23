Na, Ma = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(Na)]
Nb, Mb = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(Nb)]

result = [[0] * Mb for _ in range(Na)]
for i in range(Na):
    for j in range(Mb):
        for k in range(Ma):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(*row)