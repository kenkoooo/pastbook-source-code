# https://atcoder.jp/contests/past202004-open/submissions/20051071
# PyPy3で提出してください。

N = int(input())
# インデックスを 1 始まりにするため、先頭にダミー要素を入れる
S = " " + input()
C = [0] + list(map(int, input().split()))
D = [0] + list(map(int, input().split()))

INF = 10**100

# cost[i][j]：i 文字目までの扱いを決めて、
# そこまでの累積和が j であるときのコスト最小値
cost = []
for i in range(N+1):
    cost.append([INF]*(N+1))
cost[0][0] = 0
for i in range(1, N+1):
    for j in range(i):
        if S[i] == "(":
            # そのまま使う
            cost[i][j+1] = min(cost[i][j+1], cost[i-1][j])
            # 反転させる
            if j > 0:
                cost[i][j-1] = min(cost[i][j-1], cost[i-1][j] + C[i])
        else:
            # そのまま使う
            if j > 0:
                cost[i][j-1] = min(cost[i][j-1], cost[i-1][j])
            # 反転させる
            cost[i][j+1] = min(cost[i][j+1], cost[i-1][j] + C[i])
        # 削除する
        cost[i][j] = min(cost[i][j], cost[i-1][j] + D[i])

print(cost[N][0])