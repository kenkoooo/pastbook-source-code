# https://atcoder.jp/contests/dp/submissions/20050080

N = int(input())
h = list(map(int, input().split()))

# cost[i]:足場 i に辿り着くための最小コスト。サイズ N を確保する。
cost = [0]*N

# 初期条件。
cost[0] = 0
# 2 つ目の足場はジャンプ元が 1 通り。
cost[1] = cost[0] + abs(h[0]-h[1])
# それ以降の足場はジャンプ元が 2 通りあるため、コストが小さい方を採用する。
for i in range(2, N):
    cost[i] = min(cost[i-1] + abs(h[i-1]-h[i]), cost[i-2] + abs(h[i-2]-h[i]))

# 答えは最後の足場までの最小コスト。
print(cost[N-1])