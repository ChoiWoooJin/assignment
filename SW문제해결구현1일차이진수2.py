TC = int(input())
for tc in range(1, TC+1):

    N = float(input())
    res = ''
    for i in range(-1,-14,-1):
        res += str(int(N//(2**i)))
        N %= (2**i)
        if N == 0:
            break
    else:
        res = 'overflow'

    print(f'#{tc} {res}')

