import heapq
N, M = map(int, input().split())
# 隣接リストとしてグラフの情報を保持する配列

G = []
for _ in range(0, N):
    G.append([])
for _ in range(0, M):
    u, v, c = map(int, input().split())
    # 頂点 u から出て頂点 v へ向かう重み c の辺を保存する
    G[u].append((v, c))
    # 無向グラフとなるため、反対向きにも保存しておく
    G[v].append((u, c))

###############################
# プリム法で最小全域木問題を解く
###############################
# 頂点がマークされているかどうかを管理する配列
# 頂点 i がマークされているとき marked[i]=True となる
# 最初はどの頂点もマークされていないため N 個の False で埋めておく
marked = []
for _ in range(0, N):
    marked.append(False)

# マークされている頂点の数を保持する変数
# 最初はどの頂点もマークされていないため 0
# この値が N になったら終了する
marked_count = 0
# 最初に頂点 0 を選んでマークする
marked[0] = True
marked_count += 1
# 次に選ぶ辺の候補を入れるヒープ
Q = []
# 頂点 0 に隣接する辺を調べ、ヒープに入れる
for j, c in G[0]:
    # ヒープに選ぶ候補の辺を挿入する
    # ( 辺の重み , 選んだときにマークする頂点 ) の形式で保存する
    heapq.heappush(Q, (c, j))
# 最小全域木の重みの合計を保存する変数
sum = 0
# 全ての頂点がマークされるまで繰り返す
while marked_count < N:
    # ヒープから、最小の重みの辺を取り出す
    # これは ( 辺の重み , 選んだときにマークする頂点 ) の形式になっている
    c, i = heapq.heappop(Q)
    # 辺につながる頂点 i もすでにマークされていた場合、
    # 操作をスキップする
    if marked[i]:
        continue
    # 頂点 i をマークする
    marked[i] = True
    marked_count += 1
    # 使った辺は最小全域木となるため、重みを保存しておく
    sum += c
    # 新たにマークした頂点 i に隣接する辺を調べる
    for (j, c) in G[i]:
    # 辺がつなぐ頂点がすでにマークされていた場合はヒープに入れない
        if marked[j]:
            continue
        heapq.heappush(Q, (c, j))

# 最小全域木の重みの合計
print(sum)
