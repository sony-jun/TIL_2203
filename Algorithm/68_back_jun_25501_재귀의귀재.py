import sys

n = int(sys.stdin.readline())
string_list = []
for _ in range(n):
    string_list.append(sys.stdin.readline().rstrip("\n"))

recur_number = 1


def recursion(s, l, r):
    global recur_number
    if l >= r:
        print("1 {}".format(recur_number))
        return
    elif s[l] != s[r]:
        print("0 {}".format(recur_number))
        return
    else:
        recur_number += 1
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


for i in string_list:
    isPalindrome(i)
    recur_number = 1
