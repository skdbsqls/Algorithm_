# 1. 서로소 집합(Disjoint-sets)
# : 서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들이다.(교집합이 없다)
# - 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다.
# - 이를 대표자(representative)라고 한다.

# 2. 상호배타 집합 연산
# - Make-Set(x): 유일한 멤버(대표자) x를 포함하는 새로운 집합을 생성하는 연산
# - Find-Set(x): x를 포함하는 집합을 찾는 연산(반복)
# - Union(x, y): x와 y를 포함하는 두 집합을 통합하는 연산

# [6개의 원소(1~6)이 존재하는 경우]
# 1. 각 집합을 만들어 주는 함수
def make_set(N):
    # 1에서 n까지의 원소가 있다고 가정, 총 n개의 집합을 생성
    # 이때, 각 원소의 부모(대표자)를 자기 자신으로 초기화
    parents = [i for i in range(N + 1)]
    return parents


# 2. 대표자를 찾는 함수
def find_set(x):
    # 자기자신이 부모 노드, 즉 해당 집합의 대표자인 경우 return
    if parents[x] == x:
        return x

    # x의 부모노드를 기준으로 다시 대표자를 검색하는 과정
    return find_set(parents[x])


# 3. 두 집합을 합치는 함수
def union(x, y):
    # 1) x, y의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 2-1) 만약 이미 같은 집합이라면? 끝.
    if ref_x == ref_y:
        return

    # 2-2) 다른 집합이라면? 문제에 따라 우선되는 집합으로 합친다.(예: 더 작은 노드로 합친다)
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


N = 6
parents = make_set(N)  # parents: 해당 노드 n의 부모 정보를 가진다.
print(parents)  # [0, 1, 2, 3, 4, 5, 6]

union(1, 3)
union(2, 3)
union(5, 6)
print(parents)  # [0, 1, 1, 1, 4, 5, 5]

# 3과 5는 같은 집합인가요?
# if parents[3] == parents[5]: 노드의 부모 노드를 비교하는 것,
if find_set(3) == find_set(5):  # 반드시 대표자를 비교해야만,
    print('같은 집합입니다.')
else:
    print('다른 집합입니다.')


# 3. 연산의 효율을 높이는 방법
# 1) Rank를 이용한 Union
#    - 각 노드는 자신을 루트로 하는 subtree의 높이를 랭크(Rank)라는 이름으로 저장한다.
#    - 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다.
# 2) Path compression(경로 압축)
#    - Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어 준다.


# 경로 압축1
def find_set(x):
    # 자기자신이 부모 노드, 즉 해당 집합의 대표자인 경우 return
    if parents[x] == x:
        return x

    # 경로 압축을 통해 x의 부모를 대표자로 변경
    parents[x] = find_set(parents[x])  # 대표자를 찾아오는 재귀호출을 통해 부모를 대표자로 설정
    return parents[x]


# 경로 압축2: 할 때 마다, 모든 노드의 대표자를 변경하자!
def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]  # 경로 압축
        x = parents[x]

    return x