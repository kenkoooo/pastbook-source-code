K = int(input())
A, B = map(int, input().split())
# K の倍数が A 以上 B 以下の範囲の中にあるかどうかを記録する変数
ok = False
# K の倍数を小さい方から順番に調べる。
# i を整数として、i * K が A 以上 B 以下の範囲に入っているかを調べる。
for i in range(0, 10000000000):
    # 調べたい K の倍数が B より大きかったら、そこでループを終了する
    if i * K > B:
        break
    # 調べている K の倍数 i * K が A 以上 B 以下の範囲に入っているかを調べる。
    if A <= i * K <= B:
        ok = True
# K で割り切れる数があれば OK を出力する
if ok:
    print("OK")
else:
    print("NG")
