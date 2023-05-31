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
