"1406 에디터"

import sys
input = sys.stdin.readline

string = list(input().strip())
N = int(input())
commands = [] # 명령어 리스트

# 명령어 저장
for i in range(N):
    temp = input().strip()
    if temp == 'L' or temp == 'D' or temp == 'B':
        commands.append(temp)
    else:
        commands.append(temp.split())

# 명령어 수행
stack = []
for cmd in commands:
    if cmd == 'L':
        if string:
            stack.append(string.pop())
    elif cmd == 'D':
        if stack:
            string.append(stack.pop())
    elif cmd == 'B':
        if string:
            string.pop()
    else:
        string.append(cmd[1])

# 스택에 남아있는 문자들 가져오기
while stack:
    string.append(stack.pop())

print(''.join(string))