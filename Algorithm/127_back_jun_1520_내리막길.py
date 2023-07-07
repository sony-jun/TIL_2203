import sys

sys.setrecursionlimit(10**9)


# dfs 탐색
def dfs(x, y):
    # 목적지에 도착했으면 1을 리턴하여 목적지까지 이동한 칸 모든 칸에 1을 더한다.
    if x == m - 1 and y == n - 1:
        return 1

    # 탐색하지 않은 곳이라면 탐색
    if dp[x][y] == -1:
        dp[x][y] = 0  # 탐색 유무

        # 상/하/좌/우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고 현재 높이보다 낮은 높이라면
            if 0 <= nx < m and 0 <= ny < n:
                if graph[x][y] > graph[nx][ny]:
                    dp[x][y] += dfs(nx, ny)  # (x, y)칸까지 몇번 이동하는지

    # 탐색한 곳이거나 탐색할 수 없는 곳이라면 자기 자신을 리턴
    # 마지막에는 (0, 0)을 리턴
    return dp[x][y]


m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(dfs(0, 0))

# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# m, n = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(m)]
# dp = [[-1] * n for i in range(m)]
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]


# def is_range(x, y, now):
#     return 0 <= x < m and 0 <= y < n and arr[x][y] < now


# def solution(x, y):
#     if x == m - 1 and y == n - 1:
#         return 1
#     if dp[x][y] == -1:
#         dp[x][y] = 0
#         for i in range(4):
#             dr_x, dr_y = x + dx[i], y + dy[i]
#             if is_range(dr_x, dr_y, arr[x][y]):
#                 dp[x][y] += solution(dr_x, dr_y)

#     return dp[x][y]


# print(solution(0, 0))
