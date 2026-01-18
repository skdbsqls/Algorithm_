"16235 나무 재테크"

import sys
input = sys.stdin.readline
from collections import deque

# 봄 여름
def spring_summer(trees, ground, N):
    for i in range(N):
        for j in range(N):
            # 해당 칸에 나무가 없으면 패스
            if not trees[i][j]:
                continue
            
            new_deque = deque()  # 살아 남은 나무들을 담을 deque
            dead_nutrient = 0  # 여름에 추가될 양분

            # 나이가 어린 나무부터
            for age in trees[i][j]:
                # 나무가 양분을 먹을 수 있으면
                if ground[i][j] >= age:
                    ground[i][j] -= age  # 나이만큼 양분 먹고
                    new_deque.append(age + 1)  # 나이 한 살 추가
                # 나무가 양분을 먹을 수 없으면
                else:
                    # 죽으면서 여름에 양분으로 변환
                    dead_nutrient += age // 2

            trees[i][j] = new_deque  # 현재 칸의 나무 상태 갱신
            ground[i][j] += dead_nutrient  # 여름: 죽은 나무가 남긴 양분 추가


# 가을 겨울
def fall_winter(trees, ground, A, N):
    # 8방향
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(N):
        for j in range(N):
            # 현재 칸에 나무가 있고
            if trees[i][j]:
                for age in trees[i][j]:
                    # 그 나무의 나이가 5의 배수이면서
                    if age % 5 == 0:
                        for d in range(8):
                            ni = i + dx[d]
                            nj = j + dy[d]
                            # 땅의 범위 안에 있으면
                            if 0 <= ni < N and 0 <= nj < N:
                                # 나무 생성
                                trees[ni][nj].appendleft(1)  # 새로운 나무는 가장 앞에 넣어서 나이 오름차순 유지(!)

            # 겨울 양분 추가
            ground[i][j] += A[i][j]


N, M, K = map(int, input().split())  # N * N 땅, M개의 나무, K년 이후
A = [list(map(int, input().split())) for _ in range(N)]  # S2D2가 추가하는 양분 A[r][c]
ground = [[5] * N for _ in range(N)]  # 처음에는 모든 칸의 양분 5
trees = [[deque() for _ in range(N)] for _ in range(N)]  # 칸별로 나무 나이 저장 (deque)
for _ in range(M):
    r, c, age = map(int, input().split())
    trees[r - 1][c - 1].append(age)

# 초기 입력은 순서 보장이 없으므로, 각 칸을 나이 오름차순으로 정렬
for i in range(N):
    for j in range(N):
        if trees[i][j]:
            trees[i][j] = deque(sorted(trees[i][j]))


# K년 후 살아있는 나무의 개수
for _ in range(K):
    spring_summer(trees, ground, N)
    fall_winter(trees, ground, A, N)

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])

print(ans)