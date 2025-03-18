# 1. 백트래킹(Backtracking)
# - 여러 가지 선택지들이 존재하는 상황에서 한가지를 선택한다.
# - 선택이 이루어지면 새로운 선택지들의 집합이 생성된다.
# - 이런 선택을 반복하면서 최종 상태에 도달한다.
#     - 올바른 선택을 계속하면 목표 상태에 도달한다.
#
# [백트래킹과 깊이 우선 탐색의 차이]
# - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도 횟수를 줄임
# - 깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
# - 깊이 우선 탐색을 가하기에는 경우의 수가 너무나 많음
# - 즉, NI가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 처리 불가능
# - 백트래킹 알고리즘을 적용하면 일바적으로 경우의 수가 줄어들지만, 이 역시 최악의 경우에는 여전히
# - 지수함수 시간을 요하므로 처리 불가능

# [백트래킹 기법]
# - 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
# - 어떤 노드를 방문했을 때 그 노드를 포함한 경로가 해답이 될 수 없으면, 그 노드는 유망하지 않다고 하며,
# - 반대로 해답의 가능성이 있으면 유망하다고 함
# - 가지치기(prunning): 유망하지 않는 노드가 포함되는 경로는 더이상 고려하지 않음

# [문제] 4*4 N-Queen
# visited: (y, x) 좌표에 queen을 놓은 적이 있음을 기록
#           1) 이차원 배열로 하는 방법
#           2) 일차원 배열로 효율적으로 하는 방법

def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가
    for i in range(row):
        if visited[i][col]:
            return False

    # 2. 왼쪽 대각선에 놓은 적이 있는가
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False

        i -= 1
        j -= 1

    # 3. 오른쪽 대각선에 놓은 적이 있는가
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False

        i -= 1
        j += 1

    # [참고]
    # for i, j in zip((row - 1, -1, -1), range(col - 1, -1, -1)):
    #     if visited[i][j]:
    #         return False

    return True


# level: N개의 행에 모두 놓았다.
# branch: N개의 열
def dfs(row):
    global answer

    if row == N:  # 모두 놓으면 성공!
        answer += 1
        return

    # N개의 열에 대해 고려
    for col in range(N):
        # 만약, 기본에 같은 열이나 대각선에 놓았다면, 놓을 수 없음을 고려!(가지치기)
        if check(row, col) is False:
            continue

        visited[row][col] = 1
        dfs(row + 1)
        visited[row][col] = 0


N = 4
visited = [[0] * N for _ in range(N)]
answer = 0

dfs(0)
print(answer)

# ===================================================================================================
# [문제] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
arr = [i for i in range(1, 11)]
# visited = [] -> 여기서는 필요가 없음!

# level: N개의 원소를 모두 고려하면
# branch: 지합에 해당하는 원소를 포함 시키는 경우 or 포함 시키지 않는 경우(2)


# 누적값
# - 부분집합의 총합
# - 부분집합에 포함된 원소들
def dfs(cnt, total, subset):
    # 1. total이 10이 넘으면 출력하자
    if total == 10:
        print(subset)
        return

    # 2. total이 10이 넘으면 가지치기 하자
    if total > 10:
        return

    if cnt == 10:
        return

    dfs(cnt + 1, total + arr[cnt], subset + [arr[cnt]])  # 포함 하는 경우
    dfs(cnt + 1, total, subset)  # 집합에 포함 안 하는 경우

dfs(0, 0, [])



















