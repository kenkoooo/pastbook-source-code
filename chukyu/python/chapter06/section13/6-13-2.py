# https://atcoder.jp/contests/past201912-open/submissions/20050834

# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

N = int(input())
# 根（社長）の頂点番号
R = -1
# edges[i]: 頂点 i の子（部下）の頂点番号たち
edges = []
for i in range(N):
    edges.append([])

for i in range(N):
    p = int(input())
    if p == -1:
        R = i
    else:
        edges[p-1].append(i)

# クエリを受け取り、a の値で分類する
# queries[a]:a の値に対応する、[クエリ番号, b の値 ]を並べた配列
queries = []
for i in range(N):
    queries.append([])
Q = int(input())
for q in range(Q):
    a, b = list(map(int, input().split()))
    queries[a-1].append([q, b-1])

# 答えとなる値。True/False で格納する
ans = [False]*Q
# boss[i]: 頂点 i が今見ている頂点の上司なら True
boss = [False]*N

# 再帰関数で深さ優先探索を実装する
def dfs(i):
    # クエリを処理する
    for q, b in queries[i]:
        ans[q] = boss[b]
    # 自身を上司に設定する
    boss[i] = True
    # 再帰的に子を見ていく
    for j in edges[i]:
        dfs(j)
    # 抜けるときに自身を上司から外す
    boss[i] = False

# 根に対して呼び出す
dfs(R)

# 答えを全部まとめて出力する
for q in range(Q):
    if ans[q]:
        print("Yes")
    else:
        print("No")