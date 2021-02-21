def solve(A, R, N):
    # R=1 のとき、 N の値を無視して A を返す
    if R == 1:
        return A
    # A に R を N-1 回かける
    for _ in range(0, N - 1):
        A *= R
        # 10**9 を超えることがわかったら途中でも終了して "large" を返す
        if A > 10 ** 9:
            return "large"
    return A
A, R, N = map(int, input().split())
ans = solve(A, R, N)
print(ans)
