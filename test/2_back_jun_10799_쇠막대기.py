n = list(input())

cnt = 0
li = []

for i in range(len(n)):
    if n[i] == "(":
        li.append("(")
    else:
        if n[i - 1] == "(":
            li.pop()
            cnt += len(li)
        else:
            li.pop()
            cnt += 1
print(cnt)
