K = int(input())
A, B = map(int, input().split())
# K の倍数が A 以上 B 以下の範囲の中にあるかどうかを記録する変数
ok = False
x = A // K
u = B // K
# x < u ならば K の倍数が A 以上 B 以下の範囲の中にある
if x < u:
    ok = True
if A % K == 0:
    ok = True
# K で割り切れる数があれば OK を出力する
if ok:
    print("OK")
else:
    print("NG")
