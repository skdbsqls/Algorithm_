# 문자열 뒤집기
txt = list(input())  # input: abcde
N = len(txt)  # 문자열의 길이

for i in range(N // 2):
    txt[i], txt[N-1-i] = txt[N-1-i], txt[i]

print(txt)  # ['e', 'd', 'c', 'b', 'a']

# 파이썬에서 문자열 뒤집기(1) - 슬라이싱
s = 'string'
s = s[::-1]
print(s, type(s))  # gnirts <class 'str'>

# 파이썬에서 문자열 뒤집기(2) - list의 reverse() 메서드
s = 'string'
s_lst = list(s)  # 리스트로 변환
s_lst.reverse()  # 리스트 뒤집기

print(s_lst)  # ['g', 'n', 'i', 'r', 't', 's']
print(''.join(s_lst))  # gnirts

# 파이썬에서 문자열 뒤집기(3) - for문 활용
s = 'string'
s_list = list(s)
n = len(s_list)

for i in range(n // 2):  # 교환하는 횟수는 길이의 절반
    s_list[i], s_list[n - 1 - i] = s_list[n - 1 - i], s_list[i]

print(s_list)  # ['g', 'n', 'i', 'r', 't', 's']
print(''.join(s_lst))  # gnirts

# 연습문제 [회문1]
N = 4
word = 'CBBCBAAB'

# word의 i번째부터 N개의 글자들이 회문을 이루는지 확인
for i in range(len(word) - N + 1):
    is_palindrome = True
    for j in range(N // 2):  # 비교하는 횟수는 길이의 절반
        # i에서 N - 1칸 떨어진 글자에서 j만큼 이동한 글자의 일치 여부 확인
        if word[i + j] != word[i + N - 1 - j]:
            is_palindrome = False
            break
    if is_palindrome:
        print(word[i:i + N])

'''
CBBC
BAAB
'''

# for-else 활용하기
# else는 for문이 break에 걸리지 않고 전부 실행될 때 실행된다.
# 즉, else는 for문이 정상적으로 종료될 때만 실행된다.
txt = 'CBBCBAAB'
count = 0
for j in range(len(word) - N + 1):
    for k in range(N // 2):
        if txt[j + k] != txt[j + N - 1 - k]:
            break  # 비교 글자가 다르면 for문 중지
    else:
        count += 1

print(count)  # 2

# ========================================================================

# 문자열 비교
s1 = 'abc'
s2 = 'abc'

print(s1 == s2)  # True
print(s1 is s2)  # True

s1 = 'abc'
s2 = 'ab'
s4 = s2 + 'c'

print(s1 == s4)  # True, '=='은 같은 모양인가?
print(s1 is s4)  # False, 'is'는 같은 메모리 위치인가?

s1 = 'ab'
s2 = 'ab'
s3 = 'ac'
s4 = 'AC'
s5 = 'abc'
s6 = '1ab'

print(s1 == s2)  # True
print(s1 < s2)  # False
print(s1 < s3)  # True
print(ord('a'), ord('A'))  # 97 65, 대문자가 더 빠름
print(s1 < s5)  # True, 숫자가 더 빠름
print('A' < '@')  # False, 65 64

# 문자열 비교 함수
# - 문자열이 같으면 0
# - s1이 s2보다 사전 순서상 앞서면 -1
# - s1이 s2보다 사전 순서상 나중이면 1 리턴
def my_strcmp(s1, s2):
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

# 문자열 숫자를 정수로 변환하기
a = 'A'
b = int(a, 16)  # 16진수인 경우
print(b)  # 10

c = '1001'
d = int(c, 2)  # 2진수인 경우
print(d)  # 9