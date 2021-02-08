# https://atcoder.jp/contests/typical-algorithm/submissions/20050463

N = int(input())
A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

ALL = 1<<N

# cost[n][i]: 訪れた都市の集合が n で、最後にいる都市が i であるときのコスト最小値
cost = []
for n in range(ALL):
    cost.append([10**100]*N)

# 初期条件。最初にいるときの始点は n には含めない
cost[0][0] = 0

# n で表現される集合に要素 i が含まれるかを判定して True/False を返す関数
def has_bit(n, i):
    return (n & (1<<i) > 0)

for n in range(ALL):
    for i in range(N):
        # i からj に移動する遷移を試す
        for j in range(N):
            # すでに訪問済みか、同じ都市は無視する
            if has_bit(n, j) or i == j:
                continue
            cost[n|(1<<j)][j] = min(cost[n|(1<<j)][j], cost[n][i] + A[i][j])

# 全都市を訪問して始点に戻ってくる最小コストが答え
print(cost[ALL-1][0])