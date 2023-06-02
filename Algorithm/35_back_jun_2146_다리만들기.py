# 일단, 섬인지 아닌지를 판명부터(성공)
# 그 섬들에 이름표(?)를 붙인다(성공)

# 그 다음에 연결을 해보자 어떻게?
# 조건 : 0이 아닌 숫자일때,
# 자기 자신이 아닌 다른 숫자를 만날때까지 0 개수 세기(이걸 어떻게 하지?)
# 자기 자신과 다른 숫자를 만난다면 더한 0의 개수를 list로 보내기
# 자기 자신과 같은 숫자를 만난다면 continue 로 지나가기
# list 에 있는 숫자 중 가장 적은 수를 출력

# https://www.acmicpc.net/problem/2146


# 처음에 생각했을때 섬의 개수를 생각하지 않고 구현하는 방법을 생각해봤는데
# 섬을 구분하지 않으면 떨어져 있는 거리를 구하는 게 의미가 없음

# 4963번 섬의 개수를 참고로 한 4방향 탐색 구현

from pprint import pprint
from collections import deque


# 대각선을 사용하지 않기 때문에 4방향 탐색
def bfs(x, y):
    diff = [
        [-1, 0],
        [0, -1],
        [0, 1],
        [1, 0],
    ]

    q = deque()
    q.append((x, y))
    maps[x][y] = ans  # 방문처리

    while q:
        now = q.popleft()

        for i in range(4):
            nx = now[0] + diff[i][0]
            ny = now[1] + diff[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == 1:  # 방문하지 않았다면
                    li.append([ans, nx, ny])
                    maps[nx][ny] = ans
                    q.append((nx, ny))


# 각자의 섬마다 다른 숫자를 부여함, 여기서 거리를 어떻게 구하지?


# def bfs_2(x, y):
#     diff = [
#         [-1, 0],
#         [0, -1],
#         [0, 1],
#         [1, 0],
#     ]
#     q = deque()
#     q.append((x, y))
#     while q:
#         now = q.popleft()
#         for i in range(4):
#             nx = now[0] + diff[i][0]
#             ny = now[1] + diff[i][1]
#             if 0 < nx < n and 0 < ny < n:
#                 if maps[nx][ny] == 0:
#                     cnt += 1


n = int(input())
maps = []
ans = 1  # 섬을 표시하기 위한 숫자(대각을 제외한)


for _ in range(n):
    maps.append(list(map(int, input().split())))
li = []

# 섬끼리의 구분을 위해 이중 for문을 사용해 bfs 함수에 돌려줌
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            ans += 1
            maps[i][j] == ans
            li.append([ans, i, j])
            bfs(i, j)

# for p in range(n):
#     for q in range(n):
#         if maps[p][q] != 0:
#             maps[p][q] == 0
#             bfs_2(p, q)


pprint(maps)
pprint(li)

# 10
# 1 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 1 0 0 0 0 0 0 0 0 1


# 10
# 1 1 1 1 1 1 1 1 1 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1


# 참고: 백준 4963 섬의 개수


# from collections import deque


# def bfs(x, y):
#     diff = [
#         [-1, -1],
#         [-1, 0],
#         [-1, 1],
#         [0, -1],
#         [0, 1],
#         [1, -1],
#         [1, 0],
#         [1, 1],
#     ]  # 8방향 탐색

#     q = deque()
#     q.append((x, y))
#     maps[x][y] = 0  # 방문처리

#     while q:
#         now = q.popleft()  # 가장 먼저 들어온 값을 빼줌

#         for i in range(8):  # 8방향 탐색
#             nx = now[0] + diff[i][0]
#             ny = now[1] + diff[i][1]
#             if 0 <= nx < h and 0 <= ny < w:
#                 if maps[nx][ny] == 1:  # 방문하지 않았다면
#                     maps[nx][ny] = 0  # 방문처리 함
#                     q.append((nx, ny))


# while True:
#     w, h = map(int, input().split())
#     maps = []
#     ans = 0

#     if w == h == 0:
#         break

#     for _ in range(h):
#         maps.append(list(map(int, input().split())))

#     for i in range(h):
#         for j in range(w):
#             if maps[i][j] == 1:
#                 ans += 1  # 섬의 개수를 추가 해줌
#                 bfs(i, j)  # 1이 들어왔기 때문에, 여기서부터 섬을 찾아나가고, 나아갈곳이 없으면 끝

#     print(ans)


# 현식님 자료

# import sys
# from pprint import pprint
# from collections import deque

# input = sys.stdin.readline

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def bfs(a, b):
#     global land
#     maps[a][b] = land
#     visit[a][b] = 1

#     queue = deque()
#     queue.append((a, b))

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and maps[nx][ny]:
#                 queue.append((nx, ny))
#                 visit[nx][ny] = 1
#                 maps[nx][ny] = land

# def check(k):
#     global ans
#     dis = [[-1] * n for _ in range(n)]
#     queue = deque()


#     for i in range(n):
#         for j in range(n):
#             if maps[i][j] == k:
#                 queue.append((i, j))
#                 dis[i][j] = 0
#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < n and 0 <= ny < n:
#                 if maps[nx][ny] > 0 and maps[nx][ny] != k:

#                     ans = min(ans, dis[x][y])
#                 elif not maps[nx][ny] and dis[nx][ny] == -1:
#                     dis[nx][ny] = dis[x][y] + 1
#                     queue.append((nx, ny))

# n = int(input())

# maps = [list(map(int, input().split())) for _ in range(n)]
# visit = [[0] * n for _ in range(n)]

# land = 1

# for i in range(n):
#     for j in range(n):
#         if not visit[i][j] and maps[i][j]:
#             bfs(i, j)
#             land += 1

# ans = sys.maxsize

# for i in range(1, land):
#     check(i)
# print(ans)


# 민우님 자료


# from collections import deque

# N = int(input())

# graph = [list(map(int, input().split())) for _ in range(N)]


# res = []
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# # 섬 구별용
# def bfs(x,y):
#     graph[x][y] = 2
#     q = deque()
#     q.append((x,y))

#     while q:
#         x, y = q.popleft()

#         for a in range(4):
#             nx = x + dx[a]
#             ny = y + dy[a]

#             if 0<=nx<N and 0<=ny< N: # 섬 구별용
#                 if graph[nx][ny] == 1:
#                     graph[nx][ny] = 2
#                     q.append((nx,ny))

#                 if graph[x][y] == 2 and graph[nx][ny] == 0: # 외각 부분들 t덱큐에 넣어주기
#                     t.append((x,y))

# # 다리만들기 bfs
# def bfs2():
#     p = 0
#     while t and p==0:
#         x,y = t.popleft()

#         for a in range(4):
#             nx = x + dx[a]
#             ny = y + dy[a]

#             if 0<=nx<N and 0<=ny< N:
#                 if graph[nx][ny] == 0:
#                     graph[nx][ny] = graph[x][y] + 1
#                     t.append((nx,ny))

#                 if graph[nx][ny] == 1:
#                     res.append(graph[x][y])
#                     p +=1


# for a in range(N):
#     for b in range(N):
#         if graph[a][b] == 1:
#                 t= deque()
#                 bfs(a,b)
#                 graph2 = [p[:] for p in graph]
#                 bfs2()
#                 graph = [p[:] for p in graph2]


# print(min(res)-2)
