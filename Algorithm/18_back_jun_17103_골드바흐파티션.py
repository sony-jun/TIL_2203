from sys import stdin

array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

t = int(input())
for j in range(t):
    n = int(input())
    cnt = 0
    for k in range(2, (n // 2) + 1):
        if array[k] and array[n - k]:
            cnt += 1
    print(cnt)

# 왜 제곱근 까지만 소수를 구해야 하는가?
# 100까지 구한다고 생각했을때 11 이상은 구할 필요가 없다
# 11^2 = 121 이기때문에, 100을 넘어가는 수가 되기 때문에 소수의 제곱이 이미 100이라는 범위를 넘어가기
# 때문에
