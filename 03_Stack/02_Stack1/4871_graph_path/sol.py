import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adj_list = [[] for _ in range(V + 1)]  # 인접 리스트

    # 인접 리스트 채우기
    for edge in edges:
        start, end = edge
        adj_list[start].append(end)

        stack = []  # 스택
        visited = [0] * (V + 1)  # 방문 표시