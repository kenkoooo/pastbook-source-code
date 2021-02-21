import heapq
N, M = map(int, input().split())
# 隣接リストとしてグラフを作る
G = []
for _ in range(0, N):
    G.append([])
for _ in range(0, M):
    u, v, c = map(int, input().split())
    # u から v へと、重み c の辺が張られているため
    # 行き先の v だけでなく、重みの c も入れておく
    G[u].append((v, c))



# 頂点 0 から各頂点への最短距離を保持する配列
# N 個の -1 で満たしておく( -1 の場合は未訪問であることを表す)
dist = []
for _ in range(0, N):
    dist.append(-1)
# ダイクストラ法で使うヒープ
Q = []
# 始点となる頂点 0 をヒープに追加しておく
# ( 距離 , 頂点 ) として追加する
heapq.heappush(Q, (0, 0))
# 始点となる頂点 0 への最短距離は 0 とする
dist[0] = 0
# ヒープから取り出したことがあるかを保存する配列
# 最初は N 個の False で埋めておく
done = []
for _ in range(0, N):
    done.append(False)
# ダイクストラ法で各頂点への最短距離を求める
while len(Q) > 0:
    # ヒープの先頭の頂点を取り出して i とする
    d, i = heapq.heappop(Q)
    # もし前にヒープから取り出したことがあれば、
    # 隣接する頂点を調べるのをスキップする
    if done[i]:
        continue
    # ヒープから頂点 i を取り出したことを記録しておく
    done[i] = True
    # 頂点 i に隣接する頂点を順番に見る
    # 見ている頂点を j とする
    # また、 i から j へ移動するときに使う辺の重みを c とする
    for (j, c) in G[i]:
        # j が未訪問だったとき、あるいは j への最短距離が更新可能だったとき、
        # j への最短距離を更新して、ヒープの末尾に追加する
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heapq.heappush(Q, (dist[j], j))
print(dist[N - 1])
