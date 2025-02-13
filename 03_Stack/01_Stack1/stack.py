# 1. 스택(Stack)
# - 자료를 쌓아 올린 형태의 자료구조이다.
# - 스택에 저장된 자료는 선형 구조를 갖는다.
# - 선형 구조란? 자료 간의 관계가 1대1의 관계를 갖는다.
# - 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.

# 2. 스택의 중요한 특성
# - 마지막에 삽입한 자료를 가장 먼저 꺼낸다.
# - 후입선출(LIFO, Last-In-First-Out)이라 부른다.

# 3. 스택을 프로그램에서 구현하기 위해 필요한 자료구조와 연산
# - 자료구조란? 자료를 선형으로 저장할 저장소
# - 배열을 사용할 수 있다.
# - 저장소 자체를 스택이라 부르기도 한다.
# - 스택에서 마지막에 삽입된 원소의 위치를 'top'이라 부른다.

# 4. 스택의 연산
# - 'push' : 저장소에 자료를 저장(삽입)한다.
# - 'pop' : 저장소에서 자료를 꺼낸다(삭제한다). 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다.
# - 'isEmpty' : 스택이 공백인지 아닌지를 확인하는 연산
# - 'peek' : 스택의 top에 있는 원소를 반환하는 연산

# [스택 구현하기]
size = 10  # 스택의 크기
top = -1  # 스택의 마지막 데이터 위치
stack = [0 for _ in range(size)]  # 스택 생성

# 삽입 : push
def my_push(item):
    global top
    top += 1  # 다음 데이터가 들어갈 위치

    # 만약 top의 위치에 데이터를 넣지 못할 경우
    if top == size:
        print('overflow')
        top -= 1
    else:
        stack[top] = item


# 삭제 : pop
def my_pop():
    global top

    # 만약 top이 -1이면, 스택이 비어있는 경우
    if top == -1:
        print('is empty')
        return
    else:
        top -= 1  # 편의상 top을 먼저 하나 줄이고,
        return stack[top + 1]  # 이전 top 위치의 데이터를 반환한다.


# 비어 있는지 확인  : is_empty
def is_empty():
    return top == -1


# 다음 원소 확인 : peek
def peek():
    if top == -1:
        print('is empty')
        return
    else:
        return stack[top]


# [리스트를 스택처럼 쓰기]
stack = []

stack.append(1)  # push
stack.pop()  # pop
len(stack) == 0  # is_empty
stack[-1]  # peek


# 5. 스택의 push 알고리즘
# - 'append()'메서드를 통해 리스트의 마지막에 데이터를 삽입한다.
stack = []


def my_push(item):
    stack.append(item)


def my_push(item, size):
    global top
    top += 1

    if top == size:
        print('overflow!')
    else:
        stack[top] = item


size = 10
stack = [0] * size
top = -1

my_push(10, size)
top += 1            # push(20)을 구현하는 방법
stack[top] = 20     # top + 1 하고 stack[top] = 20

# 6. 스택의 pop 알고리즘
# - 'pop()'메서드를 통해 리스트의 마지막 데이터를 꺼낸다.


def my_pop():
    if len(stack) == 0:
        # underflow
        return
    else:
        return stack.pop()


def my_pop():
    global top

    if top == -1:  # stack이 비어있는 상황
        print('underflow')
        return 0
    else:  # 비어 있지 않으면,
        top -= 1
        return stack[top + 1]


print(my_pop())

if top > -1:                # pop() 구현하기
    top = -1                # stack이 비어 있지 않다면,
    print(stack[top + 1])   # top - 1 하고 stack[top + 1] 꺼내기

# 7. 스택의 장단점
# - 장점: 1차원 배열을 사용하여 구현할 경우 구현이 용이하다.
# - 단점: 스택의 크기를 변경하기가 어렵다.
# -> 이를 해결하기 위한 방법으로 저장소를 동적으로 할당하여 스택을 구현하는 방법이 있다.
# -> 동적 연결리스트를 이용하여 구현하는 방법을 의미한다.
# -> 이는 구현이 복잡하다는 단점이 있지만 메모리를 효율적으로 사용한다는 장점을 가진다.

