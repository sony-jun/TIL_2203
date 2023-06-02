# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYVgOZEKOpcDFAQK


res = []
for m in range(int(input())):
    res.append(int(input()) ** 2)
for i in range(len(res)):
    print("#%d %s" % (i + 1, res[i]))
