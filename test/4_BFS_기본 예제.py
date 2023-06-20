from collections import deque

N, M = map(int, input().split())
V = [0 for _ in range(N + 1)]
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

Q = deque()
# 1번 정점에서 탐색을 시작해봅시다.
V[1] = 1
Q.append(1)

# BFS는 큐에 있는 정점이 모두 없어질 때까지, 즉 모든 정점을 한 번씩 방문할 때까지 반복합니다.
while Q:
    # 가장 왼쪽에 있는 정점이 가장 먼저 들어간 정점입니다.
    cur = Q.popleft()
    # 다음으로 방문할 정점의 후보들을 추가해줍니다.
    for next in G[cur]:
        # 그래프 탐색은 모든 정점을 한 번씩만 방문해야 하므로, 이미 큐에 들어간 정점은 반드시 건너뛰어야 합니다.
        if V[next]:
            continue
        # 반드시 큐에 들어가기 전에 방문 체크를 해야합니다. 그렇지 않을 경우에는 큐에 같은 정점이 중복해서 들어가는 일이 일어납니다.
        V[next] = 1
        Q.append(next)
    print(f"현재 정점: {cur}, 다음에 방문할 정점의 순서: {Q}")

"""
위의 입력을 다시 한 번 넣어봅시다.

OUTPUT
현재 정점: 1, 다음에 방문할 정점의 순서: deque([2, 4])
현재 정점: 2, 다음에 방문할 정점의 순서: deque([4, 3, 5, 6])
현재 정점: 4, 다음에 방문할 정점의 순서: deque([3, 5, 6])
현재 정점: 3, 다음에 방문할 정점의 순서: deque([5, 6])
현재 정점: 5, 다음에 방문할 정점의 순서: deque([6])
현재 정점: 6, 다음에 방문할 정점의 순서: deque([])
"""
