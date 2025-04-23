n = int(input())
nums = list(map(int, input().split()))
x = int(input())

# 시간 초과
# count = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         if nums[i] + nums[j] == x:
#             count += 1
#
# print(count)

nums.sort()
count = 0
left, right = 0, n - 1

while left < right:
    temp = nums[left] + nums[right]

    if temp == x:
        count += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1

print(count)