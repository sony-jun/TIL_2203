n = int(input())
if n == 1:
    print(1)
if n == 2:
    print(2)
li = [0, 1, 2]
if n > 2:
    for i in range(3, 1001):
        li.append(li[i - 2] + li[i - 1])
    print(li[n] % 10007)
