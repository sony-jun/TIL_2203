from collections import deque

N, M = map(int, input().split())
# 초기에는 모든 정점의 거리를 적당히 큰 값으로 초기화해줍니다.
D = [9**9 for _ in range(N + 1)]
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

Q = deque()
# 1번 정점은 시작 정점이니 거리를 0으로 둡니다.
D[1] = 0
Q.append(1)

while Q:
    cur = Q.popleft()
    for next in G[cur]:
        # BFS는 아직 방문하지 않은 정점만 큐에 넣어야 합니다.
        # 이미 방문한 정점이라면 거리가 초기값으로 설정해둔 값보단 작을테니, 앞서 사용했던 visit 배열을 사용하지 않고도 판별이 가능합니다.
        # 추가로 큐에 들어있을 수 있는 정점들의 최단 거리는 현재 정점과 최대 1까지 밖에 차이날 수 없습니다. 왜 그런지는 한 번 생각해봅시다 :D
        if D[next] <= D[cur] + 1:
            continue
        # 다음 정점의 거리를 갱신해줍니다.
        D[next] = D[cur] + 1
        Q.append(next)
    print(f"현재 정점: {cur}, 1번 정점과 {cur}번 정점과의 최단 거리는 {D[cur]}")

"""
OUTPUT
현재 정점: 1, 1번 정점과 1번 정점과의 최단 거리는 0
현재 정점: 2, 1번 정점과 2번 정점과의 최단 거리는 1
현재 정점: 4, 1번 정점과 4번 정점과의 최단 거리는 1
현재 정점: 3, 1번 정점과 3번 정점과의 최단 거리는 2
현재 정점: 5, 1번 정점과 5번 정점과의 최단 거리는 2
현재 정점: 6, 1번 정점과 6번 정점과의 최단 거리는 2
"""
