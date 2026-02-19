"에라토스테네스의 체"

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

primes = [True for _ in range(N + 1)]
primes[0] = primes[1] = False

cnt = 0
for i in range(2, N + 1):
    if primes[i]:
        for j in range(i, N + 1, i):
            if primes[j]:
                primes[j] = False
                cnt += 1

                if cnt == K:
                    print(j)
                    break