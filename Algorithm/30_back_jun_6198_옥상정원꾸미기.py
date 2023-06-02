# https://www.acmicpc.net/problem/6198


import sys

input = sys.stdin.readline

# 처음에는 list로 다 받은 다음에 왼쪽 부터 하나씩 비교해가면서 수를 채크하는걸로 짬
# 시간 초과
# 두 번째 줄 부터 N+1번째 줄까지 각 빌딩의 높이가 hi 입력된다. (1 ≤ hi ≤ 1,000,000,000)
# 백만 * 백만이 범위를 넘어감, 즉, 이중 for문으로는 구할 수 없다는거
# stack

n = int(input())
stack = []
answer = 0
for _ in range(n):
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
