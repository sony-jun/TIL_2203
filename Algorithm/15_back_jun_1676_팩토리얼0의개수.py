n = int(input())
cnt5 = 0
for i in range(1, n + 1):
    if i % 5 == 0:
        cnt5 += 1
    if i % 25 == 0:
        cnt5 += 1
    if 1 % 125 == 0:
        cnt5 += 1
print(cnt5)
