# 부분집합 합 문제
# 유한 개의 정수로 이루어진 집합이 있을 때,
# 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지 알아내는 문제

# 1. 부분집합 생성하기
# : 집합의 원소가 n개 일 때, 공집합을 포함한 부분집합의 개수는 2^n개이다.
# : 왜? 각 원소를 부분집합에 포함시키거나 포함시키지 않는 2가지 경우를 모든 원소에 적용한 경우의 수와 같기 때문에

# 1-1) 각 원소가 부분집합에 포함되었는가를 loop를 이용하여 확인하고 부분집합을 생성하는 방법
a = [1, 2, 3]
bit = [0, 0, 0]
for i in range(2):
    bit[0] = i  # 0번 원소(0 아니면 1)
    for j in range(2):
        bit[1] = j  # 1번 원소(0 아니면 1)
        for k in range(2):
            bit[2] = k  # 2번 원소(0 아니면 1)

            sum = 0  # 부분 집합의 합
            for b in range(3):
                if bit[b]:
                    print(a[b], end=' ')  # 부분집합에 포함된 원소
                    sum += a[b]
            print(bit, sum)

# 1-2) 보다 간결하게 부분집합을 생성하는 방법
arr = [3, 6, 7]

n = len(arr)  # n : 원소의 개수

for i in range(1 << n):  # 1<<n : 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교함
        if i & (1 << j):  # i의 j번 비트가 1인 경우
            print(arr[j], end=',')  # j번 원소 출력
    print()
print()