# https://atcoder.jp/contests/dp/submissions/20050180
# PyPy3で提出してください。

N, W = list(map(int, input().split()))
# 1 始まりにするために先頭にダミーを入れる
ws = [0]
vs = [0]
for i in range(N):
    w, v = list(map(int, input().split()))
    ws.append(w)
    vs.append(v)

# value[i][w]: 品物 iまで見て重さ合計 w であるときの価値の総和の最大値
# 非常に小さい値で初期化しておく
value = []
for i in range(N+1):
    value.append([-10**18]*(W+1))

# 初期条件
value[0][0] = 0

# i が小さい順に求めていく
for i in range(1, N+1):
    for w in range(W+1):
        # 品物 i を使わない場合
        value[i][w] = max(value[i][w], value[i-1][w])
        # 品物 i を使う場合
        if w-ws[i] >= 0:
            value[i][w] = max(value[i][w], value[i-1][w-ws[i]] + vs[i])

# value[N][0], ..., value[N][W]の中で一番価値の総和が大きいものを答えとする
ans = max(value[N])
print(ans)