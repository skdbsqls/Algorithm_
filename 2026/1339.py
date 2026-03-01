"1339 단어 수학"

import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

weight = {} # 각 알파벳의 가중치

# 각 단어의 자리수에 따라 가중치 계산
for word in words:
    for idx, char in enumerate(reversed(word)):
        weight[char] = weight.get(char, 0) + (10 ** idx)

# 내림차순 정렬
sorted_weight = sorted(weight.values(), reverse=True)

# 결과 계산
result = 0
for idx, weight in enumerate(sorted_weight):
    result += weight * (9 - idx)

print(result)