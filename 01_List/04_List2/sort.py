# 1. 선택 정렬(Selection Sort)
# : 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식(오름차순 기준)

# 1-2) 정렬 과정
# - 주어진 리스트 중에서 최소값을 찾는다.
# - 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
# - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.
# - 미정렬 원소가 하나 남은 상황에서는 마지막 원소가 가장 큰 값을 갖게 되므로, 실행을 종료하고 선택 정렬이 완료된다.
# -> 시간 복잡도 : O(n^2)

# 1-3) 구현
def selection_sort(arr, N):
    # 기준 위치(최소값을 찾는 구간의 시작 인덱스)
    for i in range(N - 1):
        # 첫 원소를 최소로 가정
        min_idx = i

        # 실제 최소값을 찾는 리스트(미정렬 리스트)
        for j in range(i + 1, N):
            # 최소값을 찾으면 위치 갱신
            if arr[min_idx] > arr[j]:
                min_idx = j

        # 구간 최소값을 맨앞으로
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [64, 25, 10, 22, 11]
selection_sort(arr, len(arr))
print(arr)  # [10, 11, 22, 25, 64]

# 2. 셀렉션 알고리즘(Selection Algorithm)
# : 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
# - 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.

# 2-1) 선택 과정
# - 정렬 알고리즘을 이용하여 자료 정렬하기
# - 원하는 순서에 있는 원소 가져오기

# 2-2) 구현
# k번째로 작은 원소를 찾는 알고리즘
def select(arr, k):
    for i in range(0, k):  # k번만 반복
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[k-1]  # k번째로 작은 원소를 반환

# - 1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고, 배열의 k번째를 반환한다.
# - k가 비교적 작을 때 유용하며 O(kn)의 수행시간을 필요로 한다.

