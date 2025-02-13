# [연습문제1] 간단한 스택 구현하기
top = -1
stack = [0] * 10

# push(1)
top += 1
stack[top] = 1

# push(2)
top += 1
stack[top] = 2

# push(3)
top += 1
stack[top] = 3

# pop()
top -= 1
print(stack[top + 1])  # 3

top -= 1
print(stack[top + 1])  # 2

top -= 1
print(stack[top + 1])  # 1


# [연습문제2] 괄호 검사1
txt = '()()((()))'

top = -1
stack = [0] * 100

result = 1  # 짝이 맞다고 가정
for x in txt:
    if x == '(':  # 여는 괄호는 push, [참고] 괄호가 여러 종류인 경우, if x in '({[<'
        top += 1
        stack[top] = x
    elif x == ')':  # 닫는 괄호인 경우
        if top == -1:  # 스택이 비어 있으면,
            result = 0
            break
        else:  # 스택이 비어있지 않다면,
            top -= 1  # pop()

# 여는 괄호가 남아 있는 지 확인
# 여는 괄호가 남아 있으면,
if top > -1:
    result = 0  # 올바른 괄호가 아님

print(f'괄호 검사 결과 : {result}')  # 1


# [연습문제2] 괄호 검사1
tester = input()

# 괄호를 저장할 스택 생성하기
stack = []

# 성공 여부를 저장할 플래그 생성
success = True

# tester의 글자를 하나씩 확인하면서
for char in tester:
    # 열린 괄호라면,
    if char == "(":
        # push하기
        stack.append(char)
    elif char == ')':
        # 만약 스택이 비었다면 닫는 괄호의 짝꿍(여는 괄호)가 없다는 뜻
        if len(stack) == 0:
            # 실패
            success = False
            break
        # 스택이 비어있지 않다면 pop
        else:
            stack.pop()


# tester를 다 확인 했는데도 스택에 여는 괄호가 남아 있다면, 실패
if success:
    success = len(stack) == 0

print(success)


# [스택 응용] Function call
# - 프로그램에서 함수 호출과 복귀에 따른 수행 순서를 관리한다.
# - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조이므로,
# - 후입선출 구조의 스택을 이용하여 수행순서를 관리한다.
# - 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역 변수, 매개 변수 및 수행 후 복귀할 주소 등의 정보를
# - 스택 프레임(stack frame)에 저장하여 시스템 스택에 삽입힌다.
# - *stack[top]= 현재 실행 중인 함수
# - 함수의 실행이 끝나면 시스템 스택의 top 원소를 삭제(pop)하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀한다.
# - 함수 호출과 복귀에 따라 이 과정을 반복하면서 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.





