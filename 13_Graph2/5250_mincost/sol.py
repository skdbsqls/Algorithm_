# import sys
# sys.stdin = open('sample_in.txt')
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())  # 가로, 세로 칸 수
#     matrix = [[list(map(int, input().split()))] for _ in range(N)]
#
#     deltas = [
#         [0, 1],
#         [1, 0],
#         [0, -1],
#         [-1, 0],
#     ]
#     dists = [[1000] * N for _ in range(N)]
#     visited = [False * N for _ in range(N)]
#     dists[0][0] = 0
#
#     for i in range(N):
#         for j in range(N):
#             ni = nj = 0
#             min_dist = 1000
#
#             for delta in deltas:
#                 ti, tj = ni + delta[0], nj + delta[1]
#
#                 if 0 <= ti < N and 0 <= tj < N:
#                     if not visited[ti][tj] and dists[]