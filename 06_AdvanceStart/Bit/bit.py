# 1. 이진수로 변환하기
# 2. 각 자리를 AND, OR 연산하기

print(7 & 5)  # 5
print(7 | 5)  # 7
print(bin(7 & 5))  # 0b101

# 2진수, 16진수를 10진수로 변환하기
print(bin(10))  # 0b1010
print(hex(10))  # 0xa

# 10진수를 2진수, 16진수로 변환하기
print(int('1011', 2))  # 2진수
print(int('b', 16))  # 16진수

print(0x4A3 | 25)  # 1211
print(bin(0x4A3 | 25))  # 0b10010111011
# 0x4A3 : 1 * 3 + 16 * 10 + 16^2 * 4 (10진수)
# 0x4A3 : 0100 1010 0011 (2진수)

# [도전] 암호화 프로그램 제작하기
# 수를 입력 받고, 암호화 해주거나(인코딩), 암호를 해제해주는(디코딩) 프로그램을 제작한다.
# 단, key 값은 1004로 한다.
secret_code = 1004
print(7070 ^ secret_code)  # 6258
print(6258 ^ secret_code)  # 7070

# [도전] Left Shift(<<)를 이용한 프로그래밍
print(1 << 1, bin((1 << 1)))  # 2 0b10
print(1 << 2, bin((1 << 2)))  # 4 0b100
print(1 << 3, bin((1 << 3)))  # 8 0b1000
print(1 << 4, bin((1 << 4)))  # 16 0b10000

print(7 >> 1, bin((7 >> 1)))  # 3 0b11

num = 1
for _ in range(5):
    print(num, bin(num))
    num = num << 1
'''
1 0b1
2 0b10
4 0b100
8 0b1000
16 0b10000
'''

# [비트 연산 응용1] 1 << n
# 1. 부분집합의 수를 바로 구할 수 있다.
arr = [1, 2, 3, 4]  # 16개
print(f'부분 집합의 수: {1 << len(arr)}')

# [비트 연산 응용2] i & (1 << n)
# 부분 집합의 수만큼 반복하면서
for i in range(1 << len(arr)):  # i : 0 - 15
    for idx in range(len(arr)):  # idx : 0, 1, 2, 3
        # (1 << idx) : 0b1, ob10, ob100, ob1000
        # i 번째 부분집합에 특정 숫자가 포함되어 있는지 확인 가능
        # i의 idx번째 bit가 1인지 확인(즉, 부분 집합에 포함되어 있는지 확인)
        if i & (1 << idx):
            print(arr[idx], end=" ")
    print()
'''
1 
2 
1 2 
3 
1 3 
2 3 
1 2 3 
4 
1 4 
2 4 
1 2 4 
3 4 
1 3 4 
2 3 4 
1 2 3 4 
'''
# 합이 10인 부분 집합만 출력해보자.
arr = [1, 2, 3, 4, 5]
for i in range(1 << len(arr)):
    subset = []
    total = 0
    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]
        if total == 10:
            print(f'부분집합: {subset}')
'''
부분집합: [1, 2, 3, 4]
부분집합: [1, 2, 3, 4]
부분집합: [2, 3, 5]
부분집합: [1, 4, 5]
부분집합: [1, 2, 3, 4]
'''

# [음수 표현]
print(~4, bin(~4))  # -5 -0b101
print(~(-4))  # 3

# [도전] 비트연산 문제 풀어보기 (SWEA 10726. 이진수 표현)
# 정수 N, M이 주어질 때, M의 이진수 표현의 마지막 N비트가 모두 1로 켜져 있는지, 아닌지를 판별하여 출력하기.
# 모두 켜져있다면 ON 출력, 아니면 OFF 출력


# M의 우측 N개를 1인지 아닌지 확인할 예정
# 하나라도 0이 나오면 False
def solution():
    target = M
    # N번 확인
    for _ in range(N):
        # 맨 우측 비트가 1인지 체크
        # 0x1, ob1, 1 다 사용 가능하지만, (비트 연산이라는 것을 명시하기 위해 '0x1'를 사용)
        if target & 0x1 == 0:  # if target & 1 == 0:
            return False
        # 1이라면, 맨 우측 비트를 삭제
        target = target >> 1
    return True

# 단순하게 하는 방법
def solution2():
    # N개의 1을 구함
    mask = (1 << N) - 1
    result = (M & mask) == mask
    return result

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = solution()
