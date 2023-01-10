# 못품!
# 유클리드 호제법
# 두 양의 정수 a,b (a>b)에 대하여
# a=bq+r,(0≤ r <b)a=bq+r(0≤r<b)이라 하면,
# a,b의 최대공약수는 b,r의 최대공약수와 같다. 즉,
# gcd(a, b)=gcd(b, r)gcd(a, b)=gcd(b, r)
# r=0 이라면, a,b의 최대공약수는 b가 된다.


def gcd(x, y):  # 여기서 최대공약수를 구하나?

    return


t = int(input())
for _ in range(t):
    cnt = 0
    y = list(map(int, input().split()))
    for i in range(1, y[0]):
        for j in range(i + 1, y[0] + 1):
            for k in range(min(i, j), 0, -1):
                if j % k == 0 and i % k == 0:
                    cnt += k
                    break

        print(cnt)


"""
n = int(input())


def gcd(a, b) :
    if b==0:
        return a
    else :
        return gcd(b,a%b)


for _ in range(n):
    arr = list(map(int,input().split()))
    k = arr.pop(0)
    sum = 0
    for i in range(k):
        for j in range(k):
            if i<j :
                sum += gcd(arr[i],arr[j])
    print(sum)
"""
