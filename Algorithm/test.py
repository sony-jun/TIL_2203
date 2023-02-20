# 참고: 백준 4963 섬의 개수

from collections import deque


def bfs(x, y):
    diff = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1],
    ]  # 8방향 탐색

    q = deque()
    q.append((x, y))  # 하나씩 값을 넣어준다
    maps[x][y] = 0  # 방문처리

    while q:
        now = q.popleft()  # 가장 먼저 들어온 값을 빼줌

        for i in range(8):  # 8방향 탐색
            nx = now[0] + diff[i][0]
            ny = now[1] + diff[i][1]
            if 0 <= nx < h and 0 <= ny < w:
                if maps[nx][ny] == 1:  # 방문하지 않았다면
                    maps[nx][ny] = 0  # 방문처리 함
                    q.append((nx, ny))


while True:
    w, h = map(int, input().split())  # 행개수,열개수 입력
    maps = []
    ans = 0

    if w == h == 0:  # 0,0 입력 받으면 종료
        break

    for _ in range(h):
        maps.append(list(map(int, input().split())))  # 맵 입력

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                ans += 1  # 섬의 개수를 추가 해줌
                bfs(i, j)  # 1이 들어왔기 때문에, 여기서부터 섬을 찾아나가고, 나아갈곳이 없으면 끝

    print(ans)
