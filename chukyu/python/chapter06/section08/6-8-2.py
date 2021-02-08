# https://atcoder.jp/contests/typical-algorithm/submissions/20050573

N = int(input())

# 終了日でソートするため、[ 終了日, 開始日 ]の順に格納する
BA = []
for i in range(N):
    a, b = list(map(int, input().split()))
    BA.append([b, a])
BA.sort()

ans = 0
last = 0
for b, a in BA:
    if last < a:
        ans += 1
        last = b
print(ans)