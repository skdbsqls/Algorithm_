"9466 텀 프로젝트"

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    students = [0] + list(map(int, input().split()))
    
    visited = [0] * (N + 1)
    in_team = [0] * (N + 1) # 팀에 속한 학생 표시
    
    for start in range(1, N + 1):
        # 이미 방문한 학생이라면 건너뛰기
        if visited[start]:
            continue 
        
        path = [] # 현재 탐색 중인 경로 저장
        cur = start

        # cur 학생을 시작으로 사이클을 탐색
        while True:
    
            # 아직 방문하지 않은 학생이라면 계속 탐색
            if not visited[cur]:
                visited[cur] = 1
                path.append(cur)
                cur = students[cur]
                
            # 이미 방문한 학생이라면
            else:
                # 그 학생이 path에 있다면 사이클이 형성된 것
                if cur in path:
                    # 사이클이 시작되는 지점 찾기
                    cycle_start_index = path.index(cur)
                    # 사이클에 속한 학생들을 in_team으로 표시
                    for i in range(cycle_start_index, len(path)):
                        in_team[path[i]] = 1
                
                # 그 학생이 path에 없다면 이미 탐색이 끝난 학생
                break

    # 팀에 속한 학생 수 계산
    print(N - sum(in_team))