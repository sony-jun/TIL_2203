# 0일때 4 2*2
# 1일때 9 3*3                   1증가
# 2일때 25 5*5                 2 증가
# 3일때 81 9 *9                4 증가
# 4일때 289 17 * 17            8 증가
# 5일때 1089 33*33            16 증가
n = int(input())
a = [4]
f = 2
b = 1
sum = 0
for i in range(1, 16):
    f += b
    sum = f**2
    a.append(sum)
    b = b * 2
print(a[n])
