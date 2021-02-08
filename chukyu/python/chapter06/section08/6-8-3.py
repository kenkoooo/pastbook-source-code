# https://atcoder.jp/contests/nikkei2019-qual/submissions/20050596

N = int(input())

# A[i]+B[i] の大きい順にソートするため、
# -A[i]-B[i] を先頭に入れておく
arr = []
for i in range(N):
    a, b = list(map(int, input().split()))
    arr.append([-a-b, a, b])

arr.sort()
ans = 0
for i in range(N):
    c, a, b = arr[i]
    if i%2 == 0:
        ans += a
    else:
        ans -= b
print(ans)