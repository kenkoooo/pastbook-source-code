N, Q = map(int, input().split())
# False の N x N の2次元配列を作る
graph = []
for i in range(0, N):
    # 長さ N の False の1次元配列を作る
    row = []
    for j in range(0, N):
        row.append(False)
    # 長さ N の False の 1 次元配列を graph に追加する
    graph.append(row)

# Q 個の操作を受け取る
for i in range(0, Q):
    query = list(map(int, input().split()))
    # 頂点番号は -1する
    a = query[1] - 1

    # 「フォロー」の操作の場合
    if query[0] == 1:
        # 頂点番号は -1する
        b = query[2] - 1
        # a から b へと辺を張る
        graph[a][b] = True

    # 「フォロー全返し」の操作の場合
    if query[0] == 2:
        # 全ての頂点を順番に見る。見ている頂点を vとする
        for v in range(0, N):
            # 頂点 v から頂点 a へと辺があるとき
            if graph[v][a]:
                # 頂点 a から頂点 v へと辺を張る
                graph[a][v] = True

    # 「フォローフォロー」の操作の場合
    if query[0] == 3:
        # 頂点 a から辺を張る予定の頂点のリスト
        to_follow = []
        # 全ての頂点を順番に見る。見ている頂点を vとする
        for v in range(0, N):
            # 頂点 a から頂点 v へと辺があるとき
            if graph[a][v]:
                # さらに全ての頂点を順番に見る。見ている頂点を w とする
                for w in range(0, N):
                    # 頂点 v から頂点 w へと辺があり、かつ w が a ではないとき
                    if graph[v][w] and w != a:
                        # あとで頂点 a から辺を張るために記録しておく
                        to_follow.append(w)
        # 頂点 a から辺を張る
        for w in to_follow:
            graph[a][w] = True

# 隣接行列を全て出力する
for i in range(0, N):
    for j in range(0, N):
        # i からj へと辺がある場合は Y を、辺がない場合は N を出力する。改行はしない
        if graph[i][j]:
            print("Y", end="")
        else:
            print("N", end="")
    # N 文字出力するごとに改行する
    print()
