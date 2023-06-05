import numpy as np

n, k = map(int, input().split())

li = [[0] * (n + 2)] * (n + 2)

graph = np.array(li)

for i in range(k):
    a, b = map(int, input().split())
    graph[a][b] += 1
    graph[a][b + 1] += 1
    graph[a][b - 1] += 1
    graph[a + 1][b] += 1
    graph[a - 1][b] += 1

li_2 = graph[1 : (n + 1), 1 : (n + 1)]

print(np.sum(li_2))


# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# bomb_cnt = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# dy = [-1, 0, 0, 1]
# dx = [0, -1, 1, 0]

# for _ in range(K):
#     y, x = map(int, input().split())
#     bomb_cnt[y][x] += 1
#     for i in range(4):
#         ny, nx = y + dy[i], x + dx[i]
#         if ny < 1 or nx < 1 or ny > N or nx > N:
#             continue
#         bomb_cnt[ny][nx] += 1

# ans = 0
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         ans += bomb_cnt[i][j]

# print(ans)


# ans = 0
# for _ in range(K):
#     y, x = map(int, input().split())
#     ans += 5 - (y == 1) - (y == N) - (x == 1) - (x == N)
