# https://atcoder.jp/contests/past202005-open/submissions/20050113

N, L = list(map(int, input().split()))
X = list(map(int, input().split()))
T1, T2, T3 = list(map(int, input().split()))

# ハードルがある座標において True となるような配列
H = [False]*(L+1)
for x in X:
    H[x] = True

# cost[i]: 座標 i で行動を終了するまでの最小所要時間。
# 非常に大きな値で初期化しておき、min を用いて更新する。
cost = [10**100]*(L+1)

# 初期条件
cost[0] = 0

# 順番に求めていく
for i in range(1, L+1):
    # 行動 1
    cost[i] = min(cost[i], cost[i-1] + T1)
    # 行動 2
    if i >= 2:
        cost[i] = min(cost[i], cost[i-2] + T1 + T2)
    # 行動 3
    if i >= 4:
        cost[i] = min(cost[i], cost[i-4] + T1 + 3*T2)
    # もしハードルがあれば加算
    if H[i]:
        cost[i] += T3

# 答えは座標 L にぴったり止まるか、座標 (L-3) ～ (L-1)からジャンプ中にゴールしたもの。
ans = cost[L]
for i in [L-3, L-2, L-1]:
    if i >= 0:
        ans = min(ans, cost[i] + T1//2 + T2*(2*(L-i)-1)//2)
print(ans)