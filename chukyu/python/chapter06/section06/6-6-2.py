N = int(input())
ans = 0
# A に 1 から N-1 までの値を順番に代入して試す
for A in range(1, N):
    # A を固定したときに N>A*B を満たす正の整数 B の数
    b_count = (N - 1) // A
    ans += b_count
print(ans)
