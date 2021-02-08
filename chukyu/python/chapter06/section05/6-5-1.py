# https://atcoder.jp/contests/past201912-open/submissions/20050347

N = int(input())
A = []
for i in range(N-1):
    # A[i] は A[i][i+1]からスタートするため、0 からiまでの (i+1) 個はダミーで埋める
    lst = list(map(int, input().split()))
    A.append([0]*(i+1) + lst)

# 集合としてあり得るものの個数。2**N でも同じ
ALL = 1<<N

# happy[n]:n で表現される集合をグループにしたときの幸福度
happy = [0]*ALL

# n で表現される集合に要素 i が含まれるかを判定して True/False を返す関数
def has_bit(n, i):
    return (n & (1<<i) > 0)

# happy の値を前もって計算する
for n in range(ALL):
    for i in range(N):
        for j in range(i+1, N):
            if has_bit(n, i) and has_bit(n, j):
                happy[n] += A[i][j]

# 答えの値。非常に小さい値で初期化して、max で更新する
ans = -10**100

for n1 in range(ALL):
    for n2 in range(ALL):
        # n1 と n2 で重複があれば無視する
        if n1&n2 > 0:
            continue
        # n3 を補集合として求めて答えを更新する
        n3 = ALL-1 - (n1|n2)
        ans = max(ans, happy[n1] + happy[n2] + happy[n3])

print(ans)