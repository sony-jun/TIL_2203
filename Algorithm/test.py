import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
Y, X = map(int, input().split())

M = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
V = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    M[i] = [0] + list(map(int, input().split()))

K = M[Y][X]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
ans = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if V[i][j] or M[i][j] != K:
            continue
        Q = deque()
        V[i][j] = 1
        cnt = 0
        Q.append([i, j])
        while Q:
            cy, cx = Q.popleft()
            cnt += 1
            for k in range(4):
                ny, nx = cy + dy[k], cx + dx[k]
                if ny < 1 or nx < 1 or ny > N or nx > N:
                    continue
                if V[ny][nx] or M[ny][nx] != M[cy][cx]:
                    continue
                V[ny][nx] = 1
                Q.append([ny, nx])
        ans = max(ans, cnt)

print(ans)
