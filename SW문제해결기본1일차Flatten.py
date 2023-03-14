def dump(boxs):
    max=0
    min=101
    for i in boxs:
        if i > max:
            max = i

    for j in boxs:
        if j < min:
            min = j

    maxV = boxs.index(max)
    minV = boxs.index(min)
    boxs[maxV] = max-1
    boxs[minV] = min+1
    return max - min

tc = 10

for k in range(1, tc+1):
    N = int(input())
    box = list(map(int, input().split()))
    a = 0
    lis = []
    while a <= N:
        lis.append(dump(box))
        a = a + 1
    print(f'#{k} {lis[-1]}')


# dump(box)










