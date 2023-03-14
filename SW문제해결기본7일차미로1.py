def bfs(sr, sc):
    Q =[]
    visited = [[0]*16 for _ in range(16)]
    Q.append((sr, sc))
    visited[sr][sc] = 1
    while Q:
        sr, sc = Q.pop(0)
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            newR = sr + dr
            newC = sc + dc
            if newR>=0 and newR<16 and newC>=0 and newC<16 and arr[newR][newC] != 1 and visited[newR][newC] == 0:
                if arr[newR][newC] == 3:
                    # visited[newR][newC] = visited[sr][sc] -1
                    return 1
                else:
                    Q.append((newR, newC))
                    visited[newR][newC] = 1

    return 0






TC = 10
for tc in range(1, TC+1):
    l = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    sr=1
    sc=1
    ans = bfs(sr,sc)
    print(f'#{tc} {ans}')