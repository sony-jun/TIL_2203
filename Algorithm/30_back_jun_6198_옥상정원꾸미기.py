import sys

input = sys.stdin.readline

N = int(input())
stack = []
answer = 0
for _ in range(N):
    tower = int(input())
    if stack:
        if stack[-1] <= tower:
            while stack and stack[-1] <= tower:
                stack.pop()
            answer += len(stack)
            stack.append(tower)
        else:
            answer += len(stack)
            stack.append(tower)
    else:
        stack.append(tower)
print(answer)
