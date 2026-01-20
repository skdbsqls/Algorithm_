"17103 골드바흐 파티션"
"""
골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다
소수: 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수
"""

import sys
input = sys.stdin.readline

primes = [True for _ in range(1000001)]  # N의 최댓값이 1000000
primes[0] = primes[1] = False  # 0과 1은 소수가 아님

# 2부터 1000001까지 소수 판별하기 (에라토스테네스의 체)
for i in range(2, 1000001):
    if primes[i]:  # 해당 숫자가 소수이면 해당 수의 배수는 소수가 아님
        for j in range(i * i, 1000001, i):
            primes[j] = False

T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0  # 파티션의 개수

    for i in range(2, N // 2 + 1):  # 두 소수의 순서만 다른 것은 같은 파티션
        if primes[i] and primes[N - i]:
            cnt += 1

    print(cnt)