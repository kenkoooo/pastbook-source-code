N = int(input())
# 今までに出てきたゾロ目数の数
z = 0
# 1 から 555555 までの整数を全て調べる。調べている数を iとする
for i in range(1, 555555 + 1):
    # i がゾロ目数かどうか調べるために、i を文字列にした si を作る
    si = str(i)
    # i がゾロ目数だったかどうかを保存する変数
    ok = True
    # si の全ての文字が si の 0 文字目と同じかどうかを調べる
    # si の 0 文字目と同じ文字が含まれていたら、i はゾロ目数ではない
    for s in si:
        if s != si[0]:
            ok = False
    # i がゾロ目数のとき、出てきたゾロ目数の数を 1 増やす
    if ok:
        z += 1
    # i がゾロ目数で、N 番目に出てきたゾロ目数ならば、答えとして保存する
    if ok and z == N:
        ans = i
print(ans)
