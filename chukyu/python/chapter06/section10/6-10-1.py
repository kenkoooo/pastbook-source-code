from collections import deque
N, M = map(int, input().split())
# グラフは隣接リストとして保持する
G = []
for _ in range(0, N):
    G.append([])
# グラフの辺を受け取る
for _ in range(0, M):
    ai, bi = map(int, input().split())
    # 頂点番号は -1 して 0 から始まるようにする
    ai -= 1
    bi -= 1
    # ai と bi の間に辺を張る
    G[ai].append(bi)
    G[bi].append(ai)

########################################################
# グラフ上で幅優先探索を行い、頂点 0 から各頂点への距離を求める
########################################################

# 頂点 0 から各頂点への最短距離を保持する配列
# N 個の -1 で満たしておく( -1 の場合は未訪問であることを表す)
dist = []
for _ in range(0, N):
    dist.append(-1)
# 幅優先探索で使うキュー
Q = deque()
# 始点となる頂点 0 をキューに追加しておく
Q.append(0)
# 始点となる頂点 0 への最短距離は 0 とする
dist[0] = 0
# 幅優先探索で各頂点への最短距離を求める
while len(Q) > 0:
    # キューの先頭の頂点を取り出して i とする
    i = Q.popleft()
    # 頂点 i に隣接する頂点を順番に見る
    # 見ている頂点を j とする
    for j in G[i]:
        # j が未訪問だったとき、 j への最短距離を更新して、キューの末尾に追加する
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            Q.append(j)
if dist[N - 1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
