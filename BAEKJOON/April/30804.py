N = int(input())
arr = list(map(int, input().split()))

left = 0
fruit_count = {}
max_v = 0

for right in range(N):
    # 과일 개수 등록하기
    if arr[right] in fruit_count:
        fruit_count[arr[right]] += 1
    else:
        fruit_count[arr[right]] = 1

    # 과일의 종류가 2종류 이상이면,
    while len(fruit_count) > 2:
        fruit_count[arr[left]] -= 1  # 왼쪽부터 하나씩 빼기

        if fruit_count[arr[left]] == 0:
            del fruit_count[arr[left]]

        left += 1

    # 최대값 갱신
    max_v = max(max_v, right - left + 1)

print(max_v)