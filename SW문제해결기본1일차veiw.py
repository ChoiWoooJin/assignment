tc = 10

def myMax2(a,b,c,d):
    lis=[a,b,c,d]
    maxT = 0
    for s in lis:
        if maxT < s:
            maxT = s
    return maxT


for t in range(1, tc+1):
    N = int(input())
    BUILD = list(map(int, input().split()))
    count = 0
    for i in range(2, N-2):
        maxV = myMax2(BUILD[i-2], BUILD[i-1], BUILD[i+1], BUILD[i+2])
        if BUILD[i] > maxV:
            count = count + (BUILD[i]-maxV)
    print(f'#{t} {count}')
        #maxV랑 비교해서 count를 증가한다.















        # for j in buildings[2:building_cnt-1]:
        #     max_b = j-1  # 해당 건물의 밑층
        #     if j














