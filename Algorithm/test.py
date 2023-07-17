num_list = map(int, input().split())
answer = 0
a = 1
b = 0
for i in num_list:
    a *= i
    b += i
c = b * b
if a < b:
    answer = 1
print(answer)
