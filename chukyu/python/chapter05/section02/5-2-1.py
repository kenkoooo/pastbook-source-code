import math

N = int(input())
# N 番目のゾロ目数の桁数
x = math.ceil(N / 9)
# N 番目のゾロ目数の数字
y = N % 9
if y == 0:
    y = 9
# 答えの文字列
ans = ""
# 答えは y が x 桁並んだものとなる
for _ in range(0, x):
    ans += str(y)
print(ans)
