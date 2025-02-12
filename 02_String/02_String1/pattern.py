# 1. 고지식한 알고리즘(Brute Force)
# : 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴내의 문자들을 일일이 비교하는 방식으로 동작

def bruteforce(p, t):  # 패턴의 유무 파악하기
    N = len(t)
    M = len(p)

    i = j = 0

    while i < N and j < M:
        if t[i] != p[j]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
    if j == M:
        return i - j  # 패턴 시작 인덱스
    else:
        return -1


t = 'TTTTTATTAATA'
p = 'TTA'
print(bruteforce(p, t))  # 3


def pattern_count(p, t):  # 패턴의 등장 횟수 구하기
    N = len(t)
    M = len(p)

    i = j = 0
    cnt = 0

    while i < N and j < M:
        if t[i] != p[j]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
        if j == M:
            cnt += 1
            i = i - j + 1
            j = 0

    return cnt


t = 'TTTTTATTAATA'
p = 'TTA'
print(pattern_count(p, t))  # 2

# 고지식한 패턴 검색 알고리즘의 시간 복잡도
# : 최악의 경우 시간 복잡도는 텍스트의 모든 위치에서 패턴을 비교해야 하므로 O(MN)이 된다.

# 2. KMP 알고리즘
# : 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로,
#   불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
# KMP 알고리즘의 시간 복잡도 : O(M+N)

def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M + 1)

    j = 0
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j


# 3. 보이어-무어 알고리즘
# : 패턴에 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 무려 패턴의 길이만큼이 된다.
# - 오른쪽에서 왼쪽으로 비교

# [연습문제3] 고지식한 방법을 이용하여 패턴 찾기
def search(p, t):
    N = len(t)
    M = len(p)

    for i in range(N - M + 1):
        for j in range(M):
            if t[i + j] != p[j]:
                break
        else:
            return i
    return -1


t = 'TTTTTATTAATA'
p = 'TTA'
print(search(p, t))  # 3

# [연습문제3 - 변형] 풀이1
A = 'ABCD'
B = 'EFGHIJKLMN'

N = len(A)
M = len(B)
i = j = 0  # A[i], B[j]
ans = ''

while i + j < N + M:  # 복사할 문자가 남아있으면
    if i < N:  # A에 남은 문자가 있으면
        ans += A[i]
        i += 1
    if j < M:
        ans += B[j]
        j += 1

print(ans)  # AEBFCGDHIJKLMN

# [연습문제3 - 변형] 풀이2
A = 'ABCD'
B = 'EFGHIJKLMN'

N = len(A)
M = len(B)
i = j = 0  # A[i], B[j]
ans = [0] * (N + M)

while i + j < N + M:  # 복사할 문자가 남아있으면
    if i < N:  # A에 남은 문자가 있으면
        ans[i + j] = A[i]
        i += 1
    if j < M:
        ans[i + j] = B[j]
        j += 1

print(ans)  # ['A', 'E', 'B', 'F', 'C', 'G', 'D', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
print(''.join(ans))  # AEBFCGDHIJKLMN