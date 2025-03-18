# 1. 트리
# - 트리는 싸이클이 없는 무향 연결 그래프
# - 즉, 비선형 구조이며 원소들 간에 계층 관계를 가지는 계층형 자료구조

# 2. 이진탐색트리(BST)
# - 탐색작업을 효율적으로 하기 위한 자료구조

# 3. 힙(heap)
# - 완전 이진 트리에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해서 만든 자료구조

import heapq

arr = [20, 15, 19, 4, 13, 11]

# 1. 기본 리스트를 heap으로 만들기
heapq.heapify(arr)  # heapify: 최소힙으로 바뀜
print(arr)  # [4, 13, 11, 15, 20, 19]
# 딱 봤을 때에는 정렬이 안 된 것 처럼 보임 -> 디버깅 시 이진 트리로 그림을 그려야 함

# 2. 하니씩 데이터 추가
min_heap = []
for num in arr:
    heapq.heappush(min_heap, num)
print(min_heap)  # [4, 13, 11, 15, 20, 19]

# 최대힙?
max_heap = []
for num in arr:
    heapq.heappush(max_heap, -num)

print(max_heap)  # [-20, -15, -19, -4, -13, -11]

while max_heap:
    pop_num = heapq.heappop(max_heap)
    print(-pop_num, end=' ')  # 20 19 15 13 11 4


# [전자사전 예제]
# 1. 길이 순서로 먼저 출력
# 2. 길이가 같다면, 사전 순서로 출력
# 즉, 우선 순위가 2가지라면
arr = ['apple', 'banana', 'kiwi', 'abcd', 'abca', 'lemon', 'peach', 'grape', 'pear']
dict = []

# 단어를 (길이, 단어) 형태로 삽입
for word in arr:
    heapq.heappush(dict, (len(word), word))

# 전자사전에서 단어를 하니씩 꺼내기
print('전자사전 순서: ')
while dict:
    length, word = heapq.heappop(dict)
    print(f'{word} (길이: {length})')