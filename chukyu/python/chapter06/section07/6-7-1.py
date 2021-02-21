N = int(input())
S = input()
# 向きを変える必要がある人数の最小値を保持する変数
# 答えになりえない大きい値で初期化しておく
min_turn = 300000
sum_W = [0]
for i in range(0, N):
    if S[i] == "W":
        sum_W.append(sum_W[i] + 1)
    else:
        sum_W.append(sum_W[i])
for i in range(0, N):
    # リーダー i より西側にいて西を向いている人の数
    w = sum_W[i]
    # リーダー i より東側にいて東を向いている人の数
    e = (N - 1 - i) - (sum_W[N] - sum_W[i + 1])
    # 人 i をリーダーとしたときの
    # 向きを変える必要がある人数
    turn = w + e
    # リーダー i の場合について数え終わったら
    # 向きを変える必要がある人数の最小値を更新する
    min_turn = min(turn, min_turn)
print(min_turn)
