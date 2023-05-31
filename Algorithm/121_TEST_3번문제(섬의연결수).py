from collections import deque

n, m, k = map(int, input().split())

graph = [[] * n for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append[b]
    graph[b].append[a]

visited = [-1] * (n + 1)
q = deque()
q.append(1)

while q:
    cur = q.popleft()
    for i in graph[cur]:
        if visited[i] != -1:
            continue
        q.qppend(i)
        visited[i] = visited[cur] + 1

if 1 <= visited[n] < k:
    print("YES")
else:
    print("NO")
