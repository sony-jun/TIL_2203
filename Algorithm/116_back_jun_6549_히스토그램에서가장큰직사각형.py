import math
import sys


# sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
input = lambda: sys.stdin.readline().rstrip()
# in_range = lambda y,x: 0<=y<n and 0<=x<m
MAX = 1000000000


def make_seg(idx, s, e):
    if s == e:
        seg[idx] = histograms[s]
        return seg[idx]

    # w = e-s+1
    mid = (s + e) // 2
    l = make_seg(idx * 2, s, mid)
    r = make_seg(idx * 2 + 1, mid + 1, e)
    seg[idx] = min(l, r)
    return seg[idx]


def f(frm, to):
    if frm == to:
        return histograms[frm]

    mid = (frm + to) // 2
    l = f(frm, mid)
    r = f(mid + 1, to)

    max_val = max(l, r)

    # including border
    h = min(histograms[mid], histograms[mid + 1])
    w = 2
    s = w * h
    i, j = mid, mid + 1
    while frm < i or j < to:  # i==frm and j==to 가 되면 종료
        if j == to or frm < i and histograms[i - 1] >= histograms[j + 1]:
            i -= 1
            w += 1
            h = min(h, histograms[i])
            s = max(s, w * h)
        else:
            j += 1
            w += 1
            h = min(h, histograms[j])
            s = max(s, w * h)

    max_val = max(max_val, s)

    return max_val


while True:
    inp = list(map(int, input().split()))
    n = inp[0]
    if n == 0:
        break
    histograms = inp[1:]

    b = math.ceil(math.log2(n)) + 1
    node_n = 1 << b
    seg = [0] * node_n  # 구간의 min h 를 가짐
    make_seg(1, 0, len(histograms) - 1)

    print(f(0, len(histograms) - 1))


# import sys
# input = sys.stdin.readline


# arr = []

# while 1:
#     f_arr = list(map(int, input().rstrip().split()))
#     if f_arr[0] == 0:
#         break
#     ans = 0
#     st = []
#     arr = f_arr[1:]

#     for val in arr:
#         tmp = 0
#         while len(st) != 0 and st[-1][0] > val:
#             tmp += st[-1][1]  # 스택이 갖고 있던 밑변 값을 넘겨준다
#             ans = max(ans, tmp * st[-1][0])
#             st.pop()

#         tmp += 1
#         st.append([val, tmp])  # 높이와 밑변

#     tmp = 0
#     while len(st) != 0:  # 남은 값들 처리
#         tmp += st[-1][1]
#         ans = max(ans, tmp*st[-1][0])
#         st.pop()

#     print(ans)


# import sys
# input = sys.stdin.readline
# arr = []


# def solve(lt, rt):
#     global arr
#     if lt == rt:
#         return arr[lt]
#     mid = (lt+rt)//2
#     res = max(solve(lt, mid), solve(mid+1, rt))
#     lo = mid
#     hi = mid+1
#     height = min(arr[lo], arr[hi])
#     res = max(res, 2*height)

#     while lt < lo or hi < rt:
#         if hi < rt and (lt == lo or arr[lo-1] < arr[hi+1]):
#             hi += 1
#             height = min(height, arr[hi])
#         else:
#             lo -= 1
#             height = min(height, arr[lo])

#         res = max(res, height*(hi-lo+1))

#     return res


# while True:
#     input_arr = list(map(int, input().rstrip().split()))
#     if input_arr[0] == 0:
#         break
#     N = input_arr[0]
#     arr = input_arr[1:]
#     print(solve(0, N-1))
