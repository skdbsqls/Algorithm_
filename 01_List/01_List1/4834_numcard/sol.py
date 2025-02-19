T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    
    counts = [0] * (max(arr) + 1)
    
    for i in range(len(arr)):
        counts[arr[i]] += 1
    
    max_num = 0
    counts_num = 0
    
    for i in range(1, len(counts)):
        if max_num < i and counts_num <= counts[i]:
            counts_num = counts[i]
            max_num = i

    print(f'#{tc} {max_num} {counts_num}')