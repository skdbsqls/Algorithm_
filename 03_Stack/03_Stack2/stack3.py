# 중위 표기법
# : 연산자를 피연산자의 가운데 표기하는 방법 (A+B)

# 후위 표기법
# : 연산자를 피연사자 뒤에 표기하는 방법 (AB+)

# 중위 표기식의 후위표기식 변환 방법1
# 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현한다.
# 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동시킨다.
# 괄호를 제거한다.

# 중위 표기법에서 후위 표기법으로의 변환 알고리즘(스택 이용하기)
# 1) 입력 받은 중위 표기식에서 토큰을 읽는다.
# 2) 토큰이 피연산자이면 토큰을 출력한다.
# 3) 토큰이 연산자(괄호 포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 push하고,
#    그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop하고 토큰의 연산자를 push한다.
#    만약, top에 연산자가 없으면 push 한다.
# 4) 토큰이 오른쪽 괄호이면 스택의 top에 왼쪽 괄호가 올 때까지 스택에 pop 연산을 수행하고 pop한 연산자를 출력한다.
#    왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
# 5) 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 잉ㄺ을 것이 있다면 1부터 다시 반복한다.
# 6) 스택에 남아 있는 연산자를 모두 pop하여 출력한다.
#    * 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮다.

# 연산자 우선순위
# ) :  우선순위 없음
# *, / : 2
# +. - : 1
# ( : 스택 안(0), 스택 밖(3)

stack = [0] * 100
top = -1

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

fx = '(6+5*(2-8)/2)'
susik = ''

for x in fx:
    # 피연산자라면
    if x not in '(+-*/)':
        susik += x
    # ')'라면, ('까지 pop()
    elif x == ')':
        while stack[top] != '(':    # peek
            susik += stack[top]
            top -= 1
        top -= 1        # '(' 버림. pop()
    # '(+-*/' == 연산자라면,
    else:
        # 토큰의 우선순위가 더 높으면
        if top == -1 or isp[stack[top]] < icp[x]:
            top += 1    # push()
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1  # push()
            stack[top] = x

print(susik)


susik = '6528-*2/+'
for x in susik:
    # 피연산자라면
    if x not in '+-/*':
        top += 1  # push(x)
        stack[top] = int(x)
    # 연산자라면
    else:
        op2 = stack[top]  # pop(), 오른쪽 피연산자
        top -= 1
        op1 = stack[top]  # pop(), 왼쪽 피연산자
        top -= 1

    if x == '+':
        top += 1  # push(op1 + op2)
        stack[top] = op1 + op2
    elif x == '-':
        top += 1  # push(op1 - op2)
        stack[top] = op1 - op2
    elif x == '/':
        top += 1  # push(op1 / op2)
        stack[top] = op1 / op2
    elif x == '*':
        top += 1  # push(op1 * op2)
        stack[top] = op1 * op2

print(stack[top])


