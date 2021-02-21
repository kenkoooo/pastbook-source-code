# ∞を表す定数として、非常に大きい数を用意しておく
INF = 1_000_000_000_000_000_000
N, M = map(int, input().split())
# 全ての頂点の組についての最短距離を保存する2次元配列 dist を作る
dist = []
# 最初は辺が 1 本も張られていないため、∞の辺が張られているとして
# N x N 個の INF で埋めておく
for i in range(0, N):
    dist.append([])
    for j in range(0, N):
        dist[i].append(INF)

# グラフの辺を受け取り、 dist に直接書き込む
for _ in range(0, M):
    u, v, c = map(int, input().split())
    dist[u][v] = c

# i から i への同じ頂点同士の距離は 0 としておく
for i in range(0, N):
    dist[i][i] = 0

# ワーシャル - フロイド法
for k in range(0, N):
    for x in range(0, N):
        for y in range(0, N):
            dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])
# 全ての頂点の組について最短距離を合計する
ans = 0
for i in range(0, N):
    for j in range(0, N):
        ans += dist[i][j]
print(ans)
