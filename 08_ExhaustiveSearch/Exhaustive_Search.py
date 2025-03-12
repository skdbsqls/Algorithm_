# 1. 반복(Iteration)과 재귀(Recursion)
# - 반복과 재귀는 유사한 작업을 수행할 수 있다.
# - 반복은 수행하는 작업이 완료될 때까지 계속 반복하고,
# - 재귀는 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법이다.

# 재귀함수
def KFC(num):
    # 1) 언제 재귀호출을 정지할까?
    if num == 5:
        return

    # 2) 재귀 호출 전에 들어가야 할 로직
    print(num, end=' ')

    # 3) 다음 재귀 호출(매개변수를 변경하면서 전달)
    KFC(num + 1)

    # 4) 돌아오면서 해야할 로직
    print(num, end=' ')


KFC(0)
print('끝')

# 결과 : 0 1 2 3 4 4 3 2 1 0 끝


# ===========================================================================================
# 2. 순열(Permutation)
# - 순열? 서로 다른 N개에서, R개를 중복없이, 순서를 고려하여 나열하는 것
# - 중복순열? 서로 다른 N개에서, R개를 중복을 허용하고, 순서를 고려하여 나열하는 것

# [중복순열] 구현 원리
# 1. 재귀호출을 할 때마다, 이동 경로를 흔적으로 남긴다.
# 2. 가장 마지막 레벨에 도착했을 때, 이동 경로를 출력한다.

# [예시]
# [0, 1, 2] 3개의 카드가 존재, 2개를 뽑을 예정
path = []  # 뽑은 카드들을 저장


# cnt = 재귀호출마다 누적되어 전달되어야 하는 값
def recur(cnt):
    # 카드를 2개 뽑으면 종료
    if cnt == 2:
        # 종료 시에 해야할 로직들을 작성
        print(*path)
        return

    for num in range(3):
        path.append(num)
        recur(cnt + 1)
        path.pop()

    # 만약 카드가 1에서 6까지 6개가 있다면?
    # for num in range(1, 7):
    #     path.append(num)
    #     recur(cnt + 1)
    #     path.pop()

    # path.append(0)  # 1) 1개의 카드를 뽑는다.
    # recur(cnt + 1)  # 2) 다음 재귀 호출 시 뽑은 카드가 1개 추가되었다.
    # path.pop()  # 3) 돌아왔을 때 뽑는다.
    #
    # path.append(1)
    # recur(cnt + 1)
    # path.pop()
    #
    # path.append(2)
    # recur(cnt + 1)
    # path.pop()


# 제일 처음 호출할 때 시점, 초기값을 전달하면서 시작
recur(0)


# 중복을 취급하지 않는 [순열]을 구현하는 방법
# 1. 중복 순열 코드를 작성한다.
# 2. 중복을 제거하는 코드를 추가하면 순열 코드가 된다.

# 중복을 제거하는 원리
# - 전역 리스트를 사용하면 이미 선택했던 숫자인지 아닌지 구분할 수 있다.
# - 이를 used 배열 또는 visited 배열이라고 한다.

# [예시]
# [1, 2, 3, 4, 5, 6] 6개의 카드가 존재, 3개를 뽑을 예정
path = []  # 뽑은 카드들을 저장
used = [False] * 7  # 1에서 6까지 숫자의 사용 여부를 기록(0번 인덱스는 안 씀)

# 단, 조금 더 어려운 문제의 경우, 숫자 범위가 매우 크다면,
# 리스트 방식은 메모리 초과 가능성이 존재하기 때문에,
# dictionary(O(1))나 set(O(1))과 같은 자료구조로 해결하자!

def recur(cnt):
    # 카드를 2개 뽑으면 종료
    if cnt == 3:
        # 종료 시에 해야할 로직들을 작성
        print(*path)
        return

    for num in range(1, 7):
        # 이미 num을 뽑았다면 뽑지 말아야 한다.

        # if num in path:  # 단, 'in' 은 path의 길이를 다 본다. 즉, O(path의 길이)
        #     continue

        if used[num] is True:  # 인덱스 검색 연산은 O(1)
            continue

        used[num] = True  # 숫자의 사용 여부를 기록
        path.append(num)
        recur(cnt + 1)
        path.pop()
        used[num] = False


# 제일 처음 호출할 때 시점, 초기값을 전달하면서 시작
recur(0)


# ===========================================================================================
# 3. 완전탐색(Brute-Force)
# - 모든 가능한 경우를 모두 시도를 해보아 정답을 찾아내는 알고리즘

# [문제1] 주사위 눈금의 합
# 3개의 주사위를 던져 나올 수 있는 중복 순열에 대해, 합이 10 이하가 나오는 경우는 총 몇 가지?
path = []
result = 0


def recur(cnt, total):
    global result

    # 이미 10을 넘으면 더 이상 볼 필요가 없다.
    # -> 기저조건에서 경우의 수들을 줄여주는 기법
    if total > 10:
        return

    # 종료 조건 : 3번 던지면 끝남
    if cnt == 3:
        # 합이 10개 이하인 것은 몇 가지?

        # if sum(path) <= 10:  # 'sum'은 path 길이만큼 반복되기 때문에 비효율적 = O(N)
        #     result += 1
        #     print(path)

        if total <= 10:
            result += 1
            print(path)
        return

    # 나올 수 있는 범위는 1부터 6까지
    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1, total + num)  # 'total' 주사위 결과를 더해서 전달(누적합)
        path.pop()


recur(0, 0)  # 누적합은 매개변수로 전달하면서 풀 수 있다!


# [문제2] 연속 3장의 트럼프 카드
# A, J, Q, K 4가지 종류의 카드들이 다량으로 쌓여져 있다. 이 중에서 5장의 카드를 뽑아 나열할 때,
# 같은 종류의 카드가 3장 연속으로 나오는 경우의 수는?
card = ['A', 'J', 'Q', 'K']
path = []
result = 0


def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False


def recur(cnt):
    global result

    # 종료 조건 : 카드 5장을 뽑으면 끝남
    if cnt == 5:
        # 5장을 뽑았을 때, 연속된 카드 3장이 나오면 counting
        if count_three():
            result += 1
            print(path)
        return

    for idx in range(4):  # 카드의 종류는 4개
        path.append(card[idx])
        recur(cnt + 1)
        path.pop()


recur(0)


# 전체를 보자!
# 끝날 때 뭔 가 하자!
# 중복을 제거 하자!


# [문제3] Baby-gin(완전탐색ver)
# 0에서 9까지 번호가 적혀있는 카드가 6장이 있을 때,
# 3장의 카드가 연속적인 번호를 갖는 경우 'run'이라고 하고,
# 3장의 카드가 동일한 번호를 갖는 경우 'triplet'이라고 한다.
# 이때, 6장의 카드가 run과 triplet으로만 구성 된 경우를 'Baby-gin'이라 부른다.
# 6장의 카드 번호를 입력 받고, 완전탐색으로 Baby-gin 여부를 판단하는 프로그램을 작성하라.
# Yes/No로 출력하라.
'''
6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
'''
path = []
used = [0] * 6  # 인덱스는 0부터 5까지 있으니까 6개
result = False


def is_baby_gin():
    cnt = 0

    # run + triplet 개수의 합이 2이면 baby_gin!
    #  앞쪽 숫자 3개 체크
    a, b, c = path[0], path[1], path[2]
    if a == (b - 1) == (c - 2):  # run
        cnt += 1
    elif a == b == c:  # triplet
        cnt += 1

    # 뒤쪽 숫자 3개 체크
    a, b, c = path[3], path[4], path[5]
    if a == (b - 1) == (c - 2):  # run
        cnt += 1
    elif a == b == c:  # triplet
        cnt += 1

    return cnt == 2


def recur(cnt):
    global result

    if cnt == 6:
        # Baby-gin 검사
        if is_baby_gin():
            result = True
        return

    for idx in range(6):  # 6장의 카드 번호를 입력 받는다.
        # idx를 이미 썼다면, 뽑지 마라
        if used[idx]:
            continue

        used[idx] = 1
        path.append(arr[idx])
        recur(cnt + 1)
        path.pop()
        used[idx] = 0


arr = list(map(int, input().split()))
recur(0)

if result:
    print('YES')
else:
    print('NO')