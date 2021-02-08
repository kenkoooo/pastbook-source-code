# ビンゴカードを表す 2 次元配列となる予定の配列
A = []
for _ in range(0, 3):
    # ビンゴカードの 1 行を受けとる
    row = list(map(int, input().split()))

    # 受け取った 1 行分の配列を A の末尾に追加する
    # A は 1 次元配列を要素とする配列であるため、A は 2 次元配列である
    A.append(row)

# ビンゴカードに書かれている数字に印が付いているかどうかを記録する 2 次元配列
# 大きさは3x3
# i 行目 j 列目の数字に印が付いているとき、M[i][j]=True となるようにする
# 最初は印が付いている数字はないため、全て False にしておく
M = [[False, False, False], [False, False, False], [False, False, False]]

N = int(input())

# 選ばれた数字がビンゴカードに書かれているか確認する
for _ in range(0, N):
    # 選ばれた数字
    b = int(input())

    # b がビンゴカードに書かれているか調べる
    for i in range(0, 3):
        for j in range(0, 3):
            if A[i][j] == b:
                # もしビンゴカードの i 行目 j 列目に数字 b があれば、
                # M[i][j]=True として印を付ける
                M[i][j] = True

################################
# ビンゴを達成しているかどうかを調べる
################################
# ビンゴを達成しているかどうかを記録する変数
bingo = False

for i in range(0, 3):
    # i 行目の 3 つに印が付いているか調べる
    # 印が付いていたらビンゴ達成となる
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(0, 3):
    # i 列目の 3 つに印が付いているか調べる
    # 印が付いていたらビンゴ達成となる
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

# 左上から右下にかけて、斜めに 3 つ印が付いているか調べる
if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

# 右上から左下にかけて、斜めに 3 つ印が付いているか調べる
if M[0][2] and M[1][1] and M[2][0]:
    bingo = True

# ビンゴ達成していたら Yes を出力
if bingo:
    print("Yes")
else:
    print("No")
