





##############################################
def findCode(value):
    codes = {211:0, 221:1, 122:2, 411:3, 132:4,
             231:5, 114:6, 312:7, 213:8, 112:9
             }
    return codes[value]


def hexTobin():
    mapping = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
               '4':'0100', '5':'0101', '6':'0110', '7':'0111',
               '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
               'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111',
    }
    for rows in ARR:
        s = ''
        for hexV in rows:
            s += mapping[hexV]
        binARR.append(s)


TC = int(input())

for tc in range(1,TC+1):
    sumV = 0

    N, M = list(map(int, input().split()))
    ARR = [list(input().strip()) for _ in range(N)]

    binARR = []
    hexTobin()

    for row in range(1, N):
        col = M*4-1
        while col>54:
            if binARR[row-1][col] == '0' and binARR[row][col] == '1':
                codes = [-1] * 8
                for idx in range(8):

                    cnt1 = 0
                    while binARR[row][col] == '1':
                        col -= 1
                        cnt1 += 1

                    cnt2 = 0
                    while binARR[row][col] == '0':
                        col -= 1
                        cnt2 += 1

                    cnt3 = 0
                    while binARR[row][col] == '1':
                        col -= 1
                        cnt3 += 1

                    cnt4 = 0
                    while binARR[row][col] == '0':
                        col -= 1
                        cnt4 += 1

                    ratio = min(cnt1, cnt2, cnt3)
                    code = findCode(cnt3//ratio*100+cnt2//ratio*10+cnt1//ratio)

                    codes[7-idx] = code
                sumC = 0

                for i in range(8):
                    if i % 2 == 0:
                        sumC += codes[i]*3
                    else:
                        sumC += codes[i]

                if sumC%10 == 0:
                    sumV += sum(codes)


            else:
                col -= 1


    print(f'#{tc} {sumV}')





