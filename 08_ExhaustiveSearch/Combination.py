# 1. 부분집합
# - 집합에 포함된 원소들을 선택하는 것
# - 부분집합에는 아무것도 선택하지 않은 경우(공집합)도 집합에 포함 됨

# 집합에서 부분 집합을 찾아내는 구현 방법
# 1. 완전탐색
# 2. Binary Counting
arr = ['A', 'B', 'C']
n = len(arr)


def get_sub(tar):
    print(f'target = {tar}', end=' / ')
    for i in range(n):
        # 각각의 원소가 포함되어 있는가
        if tar & 0x1:
            print(arr[i], end='')
        tar >>= 1  # 맨 우측 비트를 삭제한다는 것은, 다음 원소를 확인한다는 것

        # if (tar >> i) & 0x1:


# 전체 부분집합 확인
for target in range(1 << n):
    get_sub(target)
    print()

'''
target = 0 / 
target = 1 / A
target = 2 / B
target = 3 / AB
target = 4 / C
target = 5 / AC
target = 6 / BC
target = 7 / ABC
'''

# [도전] 친구와 카페 방문
# 민철이는 친구 {A, B, C, D, E}가 있다. 이 중에서 최소 2명 이상의 친구를 선정하여 함께 카페를 가려고 한다.
# 총 몇 가지 경우가 가능할까?
arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)


# 1인 비트의 수를 반환하는 함수
def get_count(tar):
    cnt = 0
    for _ in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt


# 모든 부분 집합 중 원소의 수가 2개 이상인 집합의 수
ans = 0

# 모든 부분 집합을 확인
for target in range(1 << n):
    # 만약, 원소의 개수가 2개 이상이라면 ans + 1
    if get_count(target) >= 2:
        ans += 1

print(ans)  # 26

# =====================================================================================================
# 2. 조합(Combination)
# - 서로 다른 n개의 원소 중에서 r개를 순서 없이 골라낸 것

# 순열과 조합의 차이
# 순열 : A B C와 C B A는 다른 경우
# 조합 : A B C와 C B A는 같은 경우

# [도전] {A, B, C, D, E} 5명 중에서 3명을 뽑을 수 있는 모든 경우의 수
arr = ['A', 'B', 'C', 'D', 'E']
n = 3
path = []


# 5명 중에서 3명 뽑기
def recur(cnt, start):
    # N명을 뽑으면 종료!
    if cnt == n:
        print(*path)
        return

    # start : 이전 재귀로부터 넘겨받아야 하는 값
    for i in range(start, len(arr)):  # 이전에 뽑았던 인덱스 + 1부터 시작해야
        path.append(arr[i])
        # i : i번째를 뽑겠다.
        # i + 1을 매개변수로 전달 : 다음 재귀부터는 i + 1부터 고려하겠다.
        recur(cnt + 1, i + 1)
        path.pop()


recur(0, 0)


# [도전] 주사위 던지기
# 주사위 눈금 N개를 던져서 나올 수 있는 모든 조합을 출력하라
# level: 주사위 3개를 던졌을 때
# branch : 1에서 6까지 숫자
N = 3
path = []


def recur(cnt, start):
    # 종료조건: 주사위 3개를 던졌을 때
    if cnt == N:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        recur(cnt + 1, i)
        path.pop()


recur(0, 1)

















