# https://atcoder.jp/contests/past202004-open/submissions/20050246

N, M = list(map(int, input().split()))
A = []
for i in range(N):
    s = input()
    A.append(s)

# 番号ごとに座標を分類。スタートは 0, ゴールは 10 とする。
group = []
for n in range(11):
    group.append([])
for i in range(N):
    for j in range(M):
        if A[i][j] == 'S':
            n = 0
        elif A[i][j] == 'G':
            n = 10
        else:
            n = int(A[i][j])
        group[n].append([i, j])

# cost[i][j]: 数字を正しく通ってマス(i, j)に辿り着く最小移動回数。
# 非常に大きい値で初期化しておく。
cost = []
INF = 10**100
for i in range(N):
    cost.append([INF]*M)

# 初期条件。スタート地点の座標は group[0][0]。
si, sj = group[0][0]
cost[si][sj] = 0

# n が小さい方から順番に求めていく。
for n in range(1, 11):
    # 更新したいマスそれぞれについてループ。
    for i, j in group[n]:
        # 数字が n-1であるマスを全て試す。
        for i2, j2 in group[n-1]:
            cost[i][j] = min(cost[i][j], cost[i2][j2] + abs(i-i2) + abs(j-j2))

# ゴール地点の座標は group[10][0]。
# ただしゴール地点の cost が INF であれば、到達不可能なため -1を答えとする。
gi, gj = group[10][0]
ans = cost[gi][gj]
if ans == INF:
    ans = -1

print(ans)