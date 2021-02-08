# https://atcoder.jp/contests/past201912-open/submissions/20050382

N, M = list(map(int, input().split()))
# 1 始まりにするためダミーを入れる。S は整数に直す
S = [0]
C = [0]
for i in range(M):
    s, c = input().split()
    s_val = 0
    for j in range(N):
        if s[j] == 'Y':
            s_val |= 1<<j
    S.append(s_val)
    C.append(int(c))

# 集合としてあり得るものの個数。2**N でも同じ
ALL = 1<<N

# cost[i][n]: セットiまで見て揃った部品の集合が n であるときのコスト最小値
cost = []
INF = 10**100
for i in range(M+1):
    cost.append([INF]*ALL)

# 初期条件
cost[0][0] = 0

# i が小さいところから順に計算
for i in range(1, M+1):
    for n in range(ALL):
        # セットi を買わない
        cost[i][n] = min(cost[i][n], cost[i-1][n])
        # セットi を買う
        cost[i][n|S[i]] = min(cost[i][n|S[i]], cost[i-1][n] + C[i])

# 答えは部品が全部揃っている状態の最小コスト
# ただし INF のままなら、部品を揃えることは不可能
ans = cost[M][ALL-1]
if ans == INF:
    ans = -1

print(ans)