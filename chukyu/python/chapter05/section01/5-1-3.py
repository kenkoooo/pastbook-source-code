N = int(input())
S = []

for i in range(0, N):
    si = input()
    si = list(si)  # 受け取った文字列 si を文字のリストに変換する
    S.append(si)

for i in range(N - 2, -1, -1):
    for j in range(1, 2 * N - 1):
        if S[i][j] == "#":
            if S[i + 1][j - 1] == "X":
                S[i][j] = "X"
            if S[i + 1][j] == "X":
                S[i][j] = "X"
            if S[i + 1][j + 1] == "X":
                S[i][j] = "X"
for i in range(0, N):
    S[i] = "".join(S[i])  # 文字のリストS[i]を結合して、文字列に戻す
    print(S[i])
