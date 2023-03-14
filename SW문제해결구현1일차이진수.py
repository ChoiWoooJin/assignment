def hexTobin(s):
    #16진수를 10진수로
    if s.isdigit():
        decV = int(s)
    else:
        decV = ord(s) - ord('A') + 10

    #10진수를 2진수로
    res = ''
    for j in range(3,-1,-1):
        res += '1' if decV & (1<<j) else '0'

    return res


TC = int(input())
for tc in range(1, TC+1):

    N, ans = list(input().split())

    lis = []
    for i in ans:
        lis.append(hexTobin(i))

    lis = ''.join(map(str, lis))

    print(f'#{tc} {lis}')



