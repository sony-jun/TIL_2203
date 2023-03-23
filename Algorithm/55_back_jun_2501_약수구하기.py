n, k = map(int, input().split())

divisor = []

for i in range(1, n + 1):
    if n % i == 0:
        divisor.append(i)

if len(divisor) >= k:
    print(divisor[k - 1])
else:
    print(0)
