# 입력을 2차원 배열에 저장하기
'''
3
1 2 3
4 5 6
7 8 9
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

'''
3
123
456
789
'''
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]


# 0으로 채워진 3 * 4 배열 만들기
arr = [[0] * 4 for _ in range(3)]
arr = [[0 for _ in range(4)] for _ in range(3)]


# 2차원 배열 순회하기 (N * M 배열의 모든 원소를 빠짐 없이 조사하는 방법)
for i in range(N):  # i : 행의 좌표
    for j in range(M):  # j : 열의 좌표
        arr[i][j]  # 필요한 연산


# [참고] N * M 배열의 크기와 저장된 값이 주어질 때 합을 구하는 방법
'''
3 4
1 7 2 8
6 2 9 3
5 7 4 2
'''
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

sum = 0
for i in range(N):
    for j in range(M):
        sum += arr[i][j]

# [참고] 행의 합 중 최대값 구하기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0
for i in range(N):
    sum = 0
    for j in range(M):
        sum += arr[i][j]

    if max_v < sum:
        max_v = sum

# 2차원 배열에서 열 우선 순회하기
for j in range(M):  # j : 열의 좌표
    for i in range(N):  # i : 행의 좌표
        arr[i][j]  # 필요한 연산

# 2차원 배열에서 지그재그 순회하기
# 짝수 행과 홀수 행을 나눠서 생각하기 (홀수행일 때는 0에서, 짝수행일 때는 M-1에서 시작)
for i in range(N):
    for j in range(M):
        arr[i][j + (M - 1 - 2 * j) * (i % 2)]

# 2차원 배열 활용

# 2차원 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법(1)
# 인덱스 (i, j)인 칸의 상하좌우 칸 (ni, nj)

# 오른쪽 시작, 시계 방향
di = [0, 1, 0, -1]  # i를 기준으로 방향별로 더할 값
dj = [1, 0, -1, 0]  # j를 기준으로 방향별로 더할 값

# N * M  배열
for i in range(N):
    for j in range(M):
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            # 유효한 인덱스임을 확인
            if 0 <= ni < N and 0 <= nj < M:
                arr[ni][nj]

# 2차원 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법(2)
for i in range(N):
    for j in range(M):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj

            # 유효한 인덱스임을 확인
            if 0 <= ni < N and 0 <= nj < M:
                arr[ni][nj]

# 델타 응용하기
# [참고] N * N 배열에서 각 원소를 중심으로 상하좌우 K칸의 합계 중 최대값 구하기 (K = 2)
max_v = 0
for i in range(N):
    for j in range(M):
        sum = arr[i][j]  # (i, j)를 중심으로
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 상하좌우 각 방향
            for c in range(1, K + 1):  # K칸까지
                ni, nj = i + di * c, j + dj * c
                # 유효한 인덱스 확인
                if 0 <= ni < N and 0 <= nj < M:
                    sum += arr[ni][nj]
        # 최대값 업데이트
        if max_v < sum:
            max_v = sum

# [참고] 전치 행렬
# 몬 소린지 모르겠고요..~

# [연습 문제 1] 5 * 5 배열에 25개의 숫자를 저장하고, 대각선 원소의 합을 구하시오.
sum = 0
for i in range(5):
    sum += arr[i][i]
    sum += arr[i][4 - i]  # [4 - i]: N - 1 - i

# N이 홀수인 경우, 정가운데 원소는 두 번 더해지기 때문에 한 번 빼줘야 함
sum -= arr[5 // 2][5 // 2]

# [연습 문제 2] 5 * 5 배열에서 25개의 각 요소와 이숫한 요소와의 차의 절대값을 구하고,
#              25개의 요소에 대한 절대값의 총합을 구하시오.
# 단, 벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오.

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total = 0

for i in range(N):
    for j in range(N):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < N:
                total += abs(arr[ni][nj] - arr[i][j])

print(total)

























