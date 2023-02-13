# 괄호 입력
brackets = input().strip()

# 처음에 옳바는 방식의 괄호형식인지 판단
def check_brackets(bs):
    stack = []
    for b in bs:
        if b == "(" or b == "[":
            stack.append(b)
        elif b == ")" and stack:
            # 괄호 적중 제거
            if stack[-1] == "(":
                stack.pop()
            else:
                stack.append(b)
        elif b == "]" and stack:
            # 괄호 적중 제거
            if stack[-1] == "[":
                stack.pop()
            else:
                stack.append(b)
        else:
            stack.append(b)
    # for문이 끝나고 stack에 값이 있다면, 괄호가 정확히 맞지 않은 문자열.
    if stack:
        return False
    else:
        return True


# 올바른 괄호일 때의 괄호 수식
def solution(bs):
    stack = []
    for b in bs:
        if b == "(" or b == "[":
            stack.append(b)
        elif b == ")":  # and stack: x
            # 괄호 적중 () : 2
            if stack[-1] == "(":
                stack[-1] = 2
            # 겹겹이 쌓여있을 경우
            else:
                temp = 0
                # 스택은 후입 선출이므로 뒤에서부터 수식
                for i in range(len(stack) - 1, -1, -1):
                    # temp의 값 수식
                    if stack[i] == "(":
                        stack[-1] = temp * 2
                        break
                    # 스택에 숫자가 있을 경우 제거해주면서 temp에 저장
                    else:
                        temp += stack[i]
                        # print(temp)
                        stack.pop()
        elif b == "]":
            if stack[-1] == "[":
                stack[-1] = 3
            else:
                temp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == "[":
                        stack[-1] = temp * 3
                        break
                    else:
                        temp += stack[i]
                        # print(temp)
                        stack.pop()
    return sum(stack)


# 최종 괄호 수식
if check_brackets(brackets) == False:
    print(0)
else:
    print(solution(brackets))


"""
bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i - 1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i - 1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3


if stack:
    print(0)
else:
    print(answer)
"""

"""
def is_correct(string):
    stack = []
    for s in string:
        if s == "(" or s == "[":
            stack.append(s)
        
        if s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        
        if s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    
    if stack == []:
        return True
    return False


def value(string):
    stack = []
    for s in string:
        if s == "(" or s == "[":
            stack.append(s)

        if s == ")":
            if stack[-1] == "(": # 처음 넣는 경우
                stack.pop()
                stack.append(2)
            else: # 숫자가 있는 경우: 매칭 안되는 경우는 없음.
                temp_sum = stack.pop()
                a = stack[-1]
                while(type(a) == int):
                    temp_sum += stack.pop()
                    a = stack[-1]
                stack.pop()
                temp_sum *= 2
                stack.append(temp_sum)

        if s == "]":
            if stack[-1] == "[":
                stack.pop()
                stack.append(3)
            else: # 숫자가 있는 경우: 매칭 안되는 경우는 없음.
                temp_sum = stack.pop()
                a = stack[-1]
                while(type(a) == int):
                    temp_sum += stack.pop()
                    a = stack[-1]
                stack.pop()
                temp_sum *= 3
                stack.append(temp_sum)
        #print(stack)
    return(sum(stack))


string = input().strip()
if is_correct(string):
    print(value(string))
else:
    print(0)
"""
