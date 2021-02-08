# https://atcoder.jp/contests/abc129/submissions/20050725

N, M = list(map(int, input().split()))
# ok[i] = True であれば i 段目が使える
ok = [True]*(N+1)
for i in range(M):
    a = int(input())
    ok[a] = False

MOD = 10**9+7

# cnt[i]:i 段目まで辿り着く移動方法の数
cnt = [0]*(N+1)
# 初期条件
cnt[0] = 1

for i in range(1, N+1):
    if ok[i]:
        if i == 1:
            cnt[i] = cnt[i-1]
        else:
            cnt[i] = (cnt[i-1] + cnt[i-2]) % MOD

print(cnt[N])