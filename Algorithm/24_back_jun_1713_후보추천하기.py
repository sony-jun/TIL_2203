n = int(input())
m = int(input())
hubo = map(int, input().split())

li = []
num_li = []

for i in hubo:
    if i in li:
        a = li.index(i)
        num_li[a] += 1
    else:
        if len(li) >= n:
            a = num_li.index(min(num_li))
            del li[a]
            del num_li[a]
        li.append(i)
        num_li.append(1)
li.sort()
print(" ".join(map(str, li)))
