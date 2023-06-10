# cnt = 0
# li = []
# n, m = map(int, input().split())
# cnt += n
# for _ in range(m):
#     a = input().split()
#     if a[0] == "deposit":
#         cnt += int(a[1])
#     if a[0] == "pay":
#         cnt -= int(a[1])
#     if a[0] == "reservation":
#         li.append(a[1])
# for i in range(len(li)):
#     if cnt > int(li[i]):
#         cnt -= int(li[i])
#     else:
#         break

# print(cnt)

from collections import deque

N, M = map(int, input().split())
Q = deque()

for i in range(M):
    op, cost = input().split()
    cost = int(cost)

    if op == "deposit":
        N = N + cost

        while Q and Q[0] <= N:
            N = N - Q[0]
            Q.popleft()

    elif op == "pay":
        if N >= cost:
            N = N - cost

    elif op == "reservation":
        if not Q and N >= cost:
            N = N - cost
        else:
            Q.append(cost)

print(N)
