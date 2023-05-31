a, b = map(int, input().split())
ch = input()
li = input()

stack = []

ch_len = len(ch)

for i in range(len(li)):
    stack.append(li[i])
    if "".join(stack[-ch_len]) == ch:
        for j in range(ch_len):
            stack.pop()

if len(stack) == 0:
    print("EMPTY")
else:
    print("".join(stack))
