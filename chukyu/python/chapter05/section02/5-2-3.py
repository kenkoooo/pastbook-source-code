K = int(input())
A, B = map(int, input().split())
# K の倍数が A 以上 B 以下の範囲の中にあるかどうかを記録する変数
ok = False
# A から B まで順番に調べる。調べている数を x とする。
for x in range(A, B + 1):
    # 調べている数 x が K で割り切れるかどうか調べる。
    if x % K == 0:
        ok = True
# K で割り切れる数があれば OK を出力する
if ok:
    print("OK")
else:
    print("NG")
