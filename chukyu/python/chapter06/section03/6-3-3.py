# https://atcoder.jp/contests/abc114/submissions/20050058

N = int(input())

ans = 0

# 数 n について調べ、末尾に数字を追加した数を再帰的に調べる関数。
# use3, use5, use7 はそれぞれ 3, 5, 7 を使ったかというフラグ。
def dfs(n, use3, use5, use7):
    global ans
    # N を超えていたら打ち切って終了する。
    if n > N:
        return
    # 3 種類全てを使っていたら答えに加算する。
    if use3 and use5 and use7:
        ans += 1
    # 末尾に 3, 5, 7 を付けた数を再帰的に調べる。
    dfs(10*n+3, True, use5, use7)
    dfs(10*n+5, use3, True, use7)
    dfs(10*n+7, use3, use5, True)

# 何もない状態（値としては 0）から呼び出す。
dfs(0, False, False, False)

# 答えを出力する。
print(ans)