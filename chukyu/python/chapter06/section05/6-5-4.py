# https://atcoder.jp/contests/arc017/submissions/20050515

from collections import defaultdict

N, X = list(map(int, input().split()))

# 偶数番目と奇数番目で半分ずつに振り分けていく
A = []
B = []
for i in range(N):
    w = int(input())
    if i%2 == 0:
        A.append(w)
    else:
        B.append(w)

# n で表現される集合に要素 i が含まれるかを判定して
# True/False を返す関数
def has_bit(n, i):
    return (n & (1<<i) > 0)

# グループ B を全列挙して重さ合計ごとに集計
dic = defaultdict(int)
for n in range(1<<len(B)):
    s = 0
    for i in range(N):
        if has_bit(n, i):
            s += B[i]
    dic[s] += 1

# グループ A を全列挙して答えを求める
ans = 0
for n in range(1<<len(A)):
    s = 0
    for i in range(N):
        if has_bit(n, i):
            s += A[i]
    ans += dic[X-s]

print(ans)