import sys
sys.stdin = open('sample_input.txt')


# 병합
def merge(left, right):
    result = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


def merge_sort(li):
    # 분할
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    global cnt
    if left_list[-1] > right_list[-1]:
        cnt += 1

    # 병합
    merged_list = merge(left_list, right_list)
    return merged_list


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0  # 오른쪽 원소가 먼저 복사되는 경우의 수
    res = merge_sort(arr)
    ans = res[N // 2]  # N//2번째 원소

    print(f'#{tc} {ans} {cnt}')