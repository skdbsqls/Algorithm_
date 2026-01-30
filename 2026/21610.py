"21610 마법사 상어와 비바라기"

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 격자 크기, M: 이동 횟수
A = [list(map(int, input().split())) for _ in range(N)] # A: 물의 양
moves = [list(map(int, input().split())) for _ in range(M)] # moves: 이동 정보

# 초기 구름 위치
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 방향(1 ~ 8)
directions = [
    (0, -1),   
    (-1, -1),  
    (-1, 0),  
    (-1, 1),  
    (0, 1),   
    (1, 1),   
    (1, 0),  
    (1, -1),  
]

# 이동 및 비바라기 수행
for d, s in moves:
    # 구름 이동
    new_clouds = []
    for r, c in clouds:
        nr = (r + directions[d-1][0] * s) % N
        nc = (c + directions[d-1][1] * s) % N
        new_clouds.append((nr, nc))
    
    clouds = new_clouds
    
    # 비 내리기
    visited = [[0] * N for _ in range(N)]
    for r, c in clouds:
        A[r][c] += 1 # 물의 양 1 증가
        visited[r][c] = 1 # 구름이 있었던 칸 표시
    
    # 물 복사 버그
    for r, c in clouds:
        count = 0 # 대각선 방향 물의 양 세기
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and A[nr][nc] > 0:
                count += 1
        A[r][c] += count # 물의 양 증가
    
    # 새로운 구름 생성
    new_clouds = []
    for r in range(N):
        for c in range(N):
            # 구름이 없었던 칸에서 물의 양이 2 이상인 칸
            if not visited[r][c] and A[r][c] >= 2:
                A[r][c] -= 2 # 물의 양 2 감소
                new_clouds.append((r, c)) # 새로운 구름 추가
    
    clouds = new_clouds

# 물의 양 합계 계산
ans = sum(map(sum, A))

print(ans)