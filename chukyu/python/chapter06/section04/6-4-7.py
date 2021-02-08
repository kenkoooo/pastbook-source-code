# https://atcoder.jp/contests/abc026/submissions/20050274

# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

N = int(input())
# child[i]：頂点 i の子（部下）となる頂点たち
child = []
for i in range(N):
    child.append([])
for i in range(1, N):
    b = int(input())
    child[b-1].append(i)

# 再帰関数を定義する
# dfs(i): 頂点 i の子の給料を全て求め、自身の給料を計算して返す
def dfs(i):
    # 子がいなければ 1
    if len(child[i]) == 0:
        return 1
    else:
        values = []
        for j in child[i]:
            values.append(dfs(j))
        return max(values) + min(values) + 1

# 答えは頂点 0 の給料
print(dfs(0))
