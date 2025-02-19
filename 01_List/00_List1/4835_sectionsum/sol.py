import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    max_v = 0
    min_v = 0
    
    for i in range(0, M):
        max_v += arr[i]
        min_v += arr[i]
    
    for i in range(0, len(arr) - M + 1):
        sum = 0
        for j in range(i, i + M):
            sum += arr[j]
        
        if max_v < sum:
            max_v = sum

        if min_v > sum:
            min_v = sum
    
    result = max_v - min_v
    
    print(f'#{tc} {result}')