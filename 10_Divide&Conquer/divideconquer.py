# 1. 분할 정복(Divide and Conquer)
# [설계 전략]
# - 분할(Divide): 해결할 문제를 여러 개의 작은 부분으로 나눈다.
# - 정복(Conquer): 나눈 작은 문제를 각각 해결한다.
# - 통합(Combine): (필요하다면) 해결된 해답을 모은다.

# Top-Down Approach -> 재귀호출이 중심!
# 언제까지 분할 하는가? 더 이상 나눌 수 없거나, 나눌 필요가 없을 때까지


# =====================================================================================================
# 2. 병합 정렬(Merge Sort)
# : 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식이다.

# [병합 정렬 과정]
# 1. 분할 단계: 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.
# 2. 병합 단계: 2개의 부분집합을 정렬하면서 하나의 집합으로 병합한다.

# -> 병합 정렬은 외부 정렬의 기본이 되는 정렬 알고리즘으로,
#    멀티코어 CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 활용된다.


def merge(left, right):
    # 두 리스트를 병합한 결과를 담을 리스트
    result = [0] * (len(left) + len(right))
    l = r = 0

    # 두 리스트에 비교할 대상이 남아있을 때까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 데이터들 모두 result에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 오른쪽 리스트에 남은 데이터들 모두 result에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


def merge_sort(li):
    if len(li) == 1:
        return li

    # 절반씩 분할
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    # 분할이 완료되면, 병합
    merged_list = merge(left_list, right_list)

    return merged_list

arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)


# =====================================================================================================
# 3. 퀵 정렬(Quick Sort)
# : 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.

# [병합 정렬과 다른점]
# - 병합 정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, 기준 아이템(pivot item) 중심으로 분할한다.
# - 기준보다 작은 것은 왼편, 큰 것은 오른편에 위치 시킨다.
# - 각 부분 정렬이 끝난 후, 병합 정렬은 '병합'이란 후처리 작업이 필요하나, 퀵 정렬은 필요로 하지 않는다.

# 퀵 정렬은 (파티셔닝)이라는 과정을 반복하면서,
# 평균 시간 복잡도 O(nlogn)속도라는 빠른 속도로 정렬된다.

# Partitioning
# 1. 작업영역을 정한다.
# 2. 작업영역 중 가장 왼쪽에 있는 수를 Pivot이라고 하자.
# 3. Pivot을 기준으로 왼쪽에는 Pivot보다 작은 수를 배치한다.
# 4. 오른쪽에는 Pivot보다 큰 수를 배치한다.

# -> 퀵 정렬은 매우 큰 입력 데이터에 대해서 좋은 성능을 보인다.

# pivot은 제일 왼쪽 요소
def hoare_partitioning(left, right):
    pivot = arr[left]

    i = left + 1
    j = right

    while i <= j:
        # i = 큰 값을 검색하면서 오른쪽으로 진행
        while i <= j and arr[i] <= pivot:
            i += 1

        # j = 작은 값을 검색하면서 왼쪽으로 진행
        while i <= j and arr[j] >= pivot:
            j -= 1

        # SWAP
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # pivot 위치를 확정 시키기 (j와 바꾸기)
    arr[left], arr[j] = arr[j], arr[left]

    return j


# left, right: 작업 영역
def quick_sort(left, right):
    if left < right:
        # pivot을 기준으로 정렬
        pivot = hoare_partitioning(left, right)

        # 왼쪽 진행
        quick_sort(left, pivot - 1)

        # 오른쪽 진행
        quick_sort(pivot + 1, right)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr) - 1)
print(arr)


# ==========================================================================================================
# 이진 검색(Binary Search)
# : 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
# : 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행
# 단, 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

# [검색 과정]
# 1. 자료의 중앙에 있는 원소를 고른다.
# 2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
# 3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고,
#    크다면, 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
# 4. 찾고자 하는 값을 찾을 떄까지 1-3의 과정을 반복한다.

# -> 이진 검색은 정렬된 데이터를 기준으로 특정 값이나 범위를 검색하는 데 사용된다.


def binary_search_while(target):
    left = 0
    right = len(arr) - 1
    cnt = 0  # 검색 횟수

    while left <= right:
        mid = (left + right) // 2
        cnt += 1

        if arr[mid] == target:
            return mid, cnt  # mid 인덱스에서 검색 완료!

        # 왼쪽에 정답이 있는 경우
        if target < arr[mid]:
            right = mid - 1
        # 오른쪽에 정답이 있는 경우
        else:
            left = mid + 1

    return -1, cnt  # 못 찾음


# left, right를 작업 영역으로 검색
def binary_search_recur(left, right, target):
    # left <= right 만족하면 반복(종료조건)
    if left > right:
        return -1  # 못 찾음

    # 검색 완료하면 종료(종료조건)
    mid = (left + right) // 2
    if target == arr[mid]:
        return mid

    # 한 번 할 때마다 left, right를 mid를 기준으로 이동시켜면서 진행
    # 왼쪽을 봐야하는 경우
    if target < arr[mid]:
        return binary_search_recur(left, mid - 1, target)

    # 오른쪽을 봐야하는 경우
    else:
        return binary_search_recur(mid + 1, right, target)


arr = [4, 2, 9, 7, 11, 23, 19]
arr.sort()  # 이진 검색은 항상 정렬된 데이터에 적용해야 한다!
print(arr)  # [2, 4, 7, 9, 11, 19, 23]

print(binary_search_while(9))  # (3, 1)
print(binary_search_while(20))  # (-1, 3)'


print(binary_search_recur(0, len(arr) - 1, 9))  # 3
print(binary_search_recur(0, len(arr) - 1, 20))  # -1
