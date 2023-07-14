ineq, eq, n, m = input().split()
answer = 0
if ineq == "<":
    if n < m:
        answer = 1
elif ineq == "<" and eq == "=":
    if n <= m:
        answer = 1
elif ineq == ">":
    if n > m:
        answer = 1
elif ineq == ">" and eq == "=":
    if n >= m:
        answer = 1
print(answer)
