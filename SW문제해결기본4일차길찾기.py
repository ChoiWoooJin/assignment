# 행렬
def dfs(S, E):
    ST = []
    visited = [False] * (100)
    ST.append(S)
    visited[S] = True
    while ST:
        v = ST.pop()
        # if v == E:
        #     return 1

        # for w in G[v]
        for w in range(100):
            if G[v][w] and not visited[w]:
                if w == E:
                    return 1

                ST.append(w)
                visited[w] = True

    return 0

#리스트
# def dfs(S, E):
#     print(G)
#     ST = []
#     visited = [False] * 100
#
#     ST.append(S)
#     visited[S] = True
#     while ST:
#         v = ST.pop()
#
#         for w in G[v]:
#             if not visited[w]:
#                 if w == E:
#                     return 1
#                 ST.append(w)
#                 visited[w] = True
#     return 0


T = 10
for tc in range(1,11):
    tcx , num = list(map(int, input().split()))

    arr = list(map(int, input().split()))

    G = [[0]*(100) for _ in range(100)]

    for i in range(num):
        v1, v2 = arr[i*2], arr[i*2+1]
        G[v1][v2] = 1

    print(f'#{tc}', dfs(0,99))
