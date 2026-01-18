"9205 맥주 마시면서 걸어가기"
"""
맨해튼 거리 공식
두 점 (x1, y1)과 (x2, y2) 사이의 가로와 세로 이동 거리의 합으로, (|x1 - x2| + |y1 - y2|)이다.
"""

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque()
    queue.append((hx, hy))

    while(queue):
        x, y = queue.popleft()
        
        # 핵심은 현재 좌표에서 락페 좌표까지 1000m 이내면 행복하게 도착 가능이라는 점!
        if abs(x - rx) + abs(y - ry) <= 1000:
            print("happy")
            return
        
        # 1000m를 초과하는 경우 편의점을 방문해야만
        for i in range(cn):
            if not visited[i]:  # 방문하지 않았다면
                nx, ny = cl[i]

                # 해당 편의점까지 갈 수 있다면
                if abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append((nx, ny))  # 큐에 넣고
                    visited[i] = 1  # 방문처리

    print("sad")
    return

t = int(input())
for _ in range(t):
    cn = int(input())  # 편의점 개수
    cl = []  # 편의점 좌표 리스트

    hx, hy = map(int, input().split())  # 집 좌표(시작점)
    for _ in range(cn):
        cx, cy = map(int, input().split())  # 편의점 좌표
        cl.append((cx, cy))
    rx, ry = map(int, input().split())  # 락페 좌표(도착점)
    visited = [0] * cn
    bfs()
