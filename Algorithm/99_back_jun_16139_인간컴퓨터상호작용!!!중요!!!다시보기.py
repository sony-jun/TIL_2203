# 생각보다 훨씬 어려운 문제입니다!
import sys

# sys.stdin=open('input.txt')

s = sys.stdin.readline()
n = int(sys.stdin.readline())

lis = []


# @profile
def prep():
    for c in "abcdefghijklmnopqrstuvwxyz":
        cnt = 0
        tmp = []
        for item in str(s):
            if item == c:
                cnt += 1
            tmp.append(cnt)
        lis.append(tmp)


# @profile
def main():
    global n
    while n:
        n -= 1
        tmp = sys.stdin.readline().split()
        c, start, end = tmp[0], int(tmp[1]), int(tmp[2])
        tmp_lis = lis[ord(tmp[0]) - 97]
        answer = tmp_lis[end] - tmp_lis[start]
        if s[start] == c:
            answer += 1
        sys.stdout.write(str(answer) + "\n")
        # print(answer)


if __name__ == "__main__":
    prep()
    main()
