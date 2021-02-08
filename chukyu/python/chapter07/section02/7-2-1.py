# https://atcoder.jp/contests/past202005-open/submissions/20050968

import bisect

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

# B[k]: 子供 k が食べた寿司の美味しさ最大値の -1 倍
B = [0]*N

for a in A:
    # 寿司を食べる子供を二分探索で探す
    k = bisect.bisect_right(B, -a)
    if k == N:
        print(-1)
    else:
        print(k+1)
        B[k] = -a