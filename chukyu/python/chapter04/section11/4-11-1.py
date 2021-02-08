# https://atcoder.jp/contests/past202004-open/submissions/20049939

# 1. まず標準入力から文字列 S を受け取る。
S = input()

# 2. 文字 a, b, c の個数をそれぞれ数える。
na = S.count("a")
nb = S.count("b")
nc = S.count("c")

# 3. 一番多い文字を調べて、出力する。
mx = max(na, nb, nc)
if na == mx:
    print("a")
elif nb == mx:
    print("b")
elif nc == mx:
    print("c")