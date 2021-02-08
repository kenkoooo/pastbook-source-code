# https://atcoder.jp/contests/past202005-open/submissions/20050940
# PyPy3で提出してください。

from collections import deque

N, M = list(map(int, input().split()))

# 辺の隣接リスト
edges = []
for i in range(N):
    edges.append([])
for i in range(M):
    u, v = list(map(int, input().split()))
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

S = int(input())
S -= 1
K = int(input())
T = list(map(int, input().split()))
for i in range(K):
    T[i] -= 1

# 実装上、T[K] = S としておく
T.append(S)

# Dist[k][l] : 頂点 T[k]から頂点 T[l]までの移動コスト
Dist = []
for t1 in T:
    # 幅優先探索
    INF = 10**100
    dist = [INF] * N
    que = deque()
    que.append(t1)
    dist[t1] = 0
    while len(que) > 0:
        i = que.popleft()
        for j in edges[i]:
            if dist[j] == INF:
                dist[j] = dist[i] + 1
                que.append(j)        
    res = []
    for t2 in T:
        res.append(dist[t2])
    Dist.append(res)

# 巡回セールスマン問題
# cost[n][i]:T の中で訪れた頂点の集合が n で、
# 最後にいる頂点が T[i]であるときのコスト最小値
ALL = 1<<K
cost = []
for n in range(ALL):
    cost.append([INF]*K)

# 始点 S から各 T[i]に移動した状態を初期状態とする
for i in range(K):
    cost[1<<i][i] = Dist[K][i]

# n で表現される集合に要素 i が含まれるかを判定して True/False を返す関数
def has_bit(n, i):
    return (n & (1<<i) > 0)

for n in range(ALL):
    for i in range(K):
        # i からj に移動する遷移を試す
        for j in range(K):
            # すでに訪問済みか、同じ頂点は無視する
            if has_bit(n, j) or i == j:
                continue
            # 事前計算した T[i]から T[j] への最小距離を使う
            cost[n|(1<<j)][j] = min(cost[n|(1<<j)][j], cost[n][i] + Dist[i][j])

# K 個の頂点を全て訪問して、どこかの頂点にいる中での最小コストが答え
print(min(cost[ALL-1]))