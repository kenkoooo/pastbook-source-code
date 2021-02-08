# https://atcoder.jp/contests/dp/submissions/20050310

# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

N, M = list(map(int, input().split()))

# edges[i]: 頂点 i から辺が伸びている頂点たち（隣接リスト）
edges = []
for i in range(N):
    edges.append([])
# 入次数。始点の判定に使う
indeg = [0]*N

# 辺の入力を受け取り、隣接リストを作る
for i in range(M):
    x, y = list(map(int, input().split()))
    edges[x-1].append(y-1)
    indeg[y-1] += 1

# length[i]: 頂点 i から始まるパスの最大長
length = [0]*N
# done[i]:cost[i] がすでに計算済みであることを示すフラグ
done = [False]*N

# メモ化再帰の実装。
def rec(i):
    # 計算済みであれば、即座に値を返す
    if done[i]:
        return length[i]
    # そうでなければ値を計算する
    length[i] = 0
    for j in edges[i]:
        length[i] = max(length[i], rec(j) + 1)
    # 計算済みフラグを立てて値を返す
    done[i] = True
    return length[i]

# 始点全てについてrec を呼び出す
for i in range(N):
    if indeg[i] == 0:
        rec(i)

# 答えは length の最大値
print(max(length))