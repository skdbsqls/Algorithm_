import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    primes = {
        2: 0,
        3: 0,
        5: 0,
        7: 0,
        11: 0,
    }
    i = 2
    while i <= N:
        if N % i == 0:
            primes[i] += 1
            N = N / i
        else:
            i += 1

    result = primes.values()

    print(f'#{tc} {" ".join(map(str, result))}')