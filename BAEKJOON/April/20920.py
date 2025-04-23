import sys
# sys.stdin.readline()

N, M = map(int, input().split())
words = [input() for _ in range(N)]

# 각 단어의 등장 횟수와 길이 구하기
dict = {}
for word in words:
    if len(word) < M:  # 길이가 M 미만인 단어는 pass
        continue

    if dict.get(word):
        dict[word][0] += 1
    else:
        dict[word] = [1, len(word)]

# 등장 횟수와 길이를 기준으로 정렬하기
# sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
# -> [('swift', [3, 5]), ('mouse', [2, 5]), ('appearance', [1, 10]), ('attendance', [1, 10]), ('wallet', [1, 6]), ('append', [1, 6])]
sorted_dict = sorted(dict.items(), key=lambda item: (-item[1][0], -item[1][1], item[0]))
# -> [('swift', [3, 5]), ('mouse', [2, 5]), ('appearance', [1, 10]), ('attendance', [1, 10]), ('append', [1, 6]), ('wallet', [1, 6])]

# 출력
for i in range(len(sorted_dict)):
    print(sorted_dict[i][0])