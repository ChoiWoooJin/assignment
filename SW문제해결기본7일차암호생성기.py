TC = 10
for tc in range(1,TC+1):
    h = int(input())

    arr = list(map(int, input().split()))
    # print(arr)

    # print(t)
    minus = 1
    while arr.count(0) != 1:
        # global arr
        t = arr.pop(0)
        t -= minus
        if t >= 1:

            arr.append(t)
            minus += 1
            if minus > 5:
                minus = 1
        else:
            arr.append(0)
            break

    print(f'#{tc}', *arr)




