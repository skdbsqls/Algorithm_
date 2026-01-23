"16637 괄호 추가하기"

import sys
input = sys.stdin.readline

# 계산
def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    
# 재귀
def recur(idx, cur): # 지금 처리할 연산자의 인덱스, 지금까지 계산된 값
    global ans, nums, ops

    # 연산자를 다 썼으면 최댓값 갱신
    if idx == len(ops):
        ans = max(ans, cur)
        return

    # 1) 괄호 없이 현재 연산자를 사용하는 경우
    no_bracket = calc(cur, ops[idx], nums[idx + 1])
    recur(idx+ 1, no_bracket)

    # 2) 다음 연산을 괄호로 먼저 계산하는 경우 
    if idx + 1 < len(ops): # idx + 1 연산자가 있어야 가능함
        # 괄호 먼저 계산하기
        inside = calc(nums[idx + 1], ops[idx + 1], nums[idx + 2])
        with_bracket = calc(cur, ops[idx], inside)
        recur(idx + 2, with_bracket) # 다음 연산자는 이미 괄호 안에서 처리됨(겹치면 안 됨)


N = int(input())
expr = input().strip()

nums = [] # 숫자
ops = [] # 연산자
for idx, ch in enumerate(expr):
    if idx % 2 == 0:
        nums.append(int(ch))
    else:
        ops.append(ch)

ans = -2**31 # 최솟값

recur(0, nums[0])
print(ans)