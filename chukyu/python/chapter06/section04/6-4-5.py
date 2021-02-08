# https://atcoder.jp/contests/tdpc/submissions/20050213

N = int(input())
# 1 始まりにするために先頭にダミーを入れる
ps = [0] + list(map(int, input().split()))

P = sum(ps)

# exist[i][s]:iまでの問題で得点合計を s にできる
exist = []
for i in range(N+1):
    exist.append([False]*(P+1))

# 初期条件
exist[0][0] = True

# i が小さい順に exist の値を求めていく
for i in range(1, N+1):
    for s in range(P+1):
        # 問題 i を解かない場合
        if exist[i-1][s]:
            exist[i][s] = True
        # 問題 i を解く場合
        if s >= ps[i] and exist[i-1][s-ps[i]]:
            exist[i][s] = True

# 答えは exist[N][s]の中で True になっている s の個数
ans = 0
for s in range(P+1):
    if exist[N][s]:
        ans += 1

print(ans)