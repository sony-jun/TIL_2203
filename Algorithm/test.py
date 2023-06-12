import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = input().rstrip()
Q = []
Q.append(("", 1))

S += "z"
for c in S:
    if Q[-1][0] != c:
        if M <= Q[-1][1]:
            top = Q[-1][0]
            while top == Q[-1][0]:
                Q.pop()
    if Q[-1][0] == c:
        Q.append((c, Q[-1][1] + 1))
        print(Q)
    else:
        Q.append((c, 1))
        print(Q)
Q.pop()
print(Q)

if len(Q) > 1:
    for c, n in Q:
        print(c, end="")
else:
    print("CLEAR!")
