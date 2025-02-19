nums = [55, 7, 78, 12, 42]
n = 5

for i in range(n - 1, 0, -1):
    for j in range(i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)  # [7, 12, 42, 55, 78]


nums = [55, 7, 78, 12, 42]
n = 5
for i in range(n):
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)  # [7, 12, 42, 55, 78]


def bubble_sort(nums):
    n = 0
    for _ in nums:
        n += 1

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


data = [9, 2, 421, 5674, 325]
print(bubble_sort(data))  # [2, 9, 325, 421, 5674]