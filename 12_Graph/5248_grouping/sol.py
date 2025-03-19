import sys
sys.stdin = open('sample_input.txt')


# 1. 집합 만들기
def make_set(N):
    parents = [i for i in range(N + 1)]
    return parents


# 2. 대표자 찾기
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


# 3. 집합 합치기(조 만들기)
def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return
    elif ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N명, M장의 신청서
    arr = list(map(int, input().split()))

    # 집합 만들기
    parents = make_set(N)

    # 집합 합치기(조 만들기)
    for i in range(0, len(arr), 2):
        x = arr[i]
        y = arr[i + 1]

        union(x, y)

    # 총 몇 개의 조?
    ans = []
    for i in range(1, len(parents)):
        if find_set(i) not in ans:
            ans.append(find_set(i))

    print(f'#{tc} {len(ans)}')