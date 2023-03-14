# import sys
# sys.stdin = open('input (20).txt', 'r')
#
#
# TC = 10
# for _ in range(1, TC+1):
#     tc = int(input())
#
#
#     array = [list(map(int, input().split())) for _ in range(100)]
#     lis = []
#
#     for row in range(100):
#         sumV = 0
#         for col in range(100):
#             sumV += array[row][col]
#         lis.append(sumV)
#
#     for col in range(100):
#         sumV = 0
#         for row in range(100):
#             sumV += array[row][col]
#         lis.append(sumV)
#
#     sumV = 0
#     for row in range(100):
#
#         sumV += array[row][row]
#     lis.append(sumV)
#
#     sumV = 0
#     for row in range(100):
#
#         sumV += array[row][99-row]
#     lis.append(sumV)
#
#     maxV = 0
#     for c in lis:
#         if c > maxV:
#             maxV = c
#
#
#     print(f'#{tc} {maxV}')


###############################################################################################

# TC = 10
# for tc in range(1, TC+1):
#     ew = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#
#     lis1 =[]
#     for r in range(100):
#         sum1 = 0
#
#         for c in range(100):
#             sum1 += arr[r][c]
#         lis1.append(sum1)
#
#     a = max(lis1)
#
#     lis2 =[]
#     for r in range(100):
#         sum2 = 0
#         for c in range(100):
#             sum2 += arr[c][r]
#         lis2.append(sum2)
#
#     b = max(lis2)
#     # print(lis2)
#
#     sum3=0
#
#     for r in range(100):
#         for c in range(100):
#             if r == c:
#                 sum3 += arr[r][c]
#
#     sum4 = 0
#     for r in range(100):
#         for c in range(100):
#
#             if r + c == 99:
#                 sum4 += arr[r][99 - c]
#
#
#     lis3 = [a,b,sum3,sum4]
#     maxC = max(lis3)
#     print(f'#{tc} {maxC}')

##############################################################

import sys
sys.stdin=open('input.txt', 'r')

TC = 10
for tc in range(1, TC+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]


    sumV_row = 0

    for row in range(100):
        cnt_row = 0
        for col in range(100):
            cnt_row += arr[row][col]
        if cnt_row > sumV_row:
            sumV_row = cnt_row

    # print(sumV_row)

    sumV_col = 0

    for col in range(100):
        cnt_col = 0
        for row in range(100):
            cnt_col += arr[row][col]
        if cnt_col > sumV_col:
            sumV_col = cnt_col

    # print(sumV_col)

    sumV_L = 0

    for row in range(100):
        cnt_L = 0
        for col in range(100):
            if row == col:
                cnt_L += arr[row][col]
        if cnt_L > sumV_L:
            sumV_L = cnt_L

    # print(sumV_L)

    sumV_R = 0
    for row in range(100):
        cnt_R = 0
        for col in range(99,-1,-1):
            if row == 100-col:
                cnt_R += arr[row][col]
        if cnt_R > sumV_R:
            sumV_R = cnt_R

    ans_lis = [sumV_row, sumV_col, sumV_L, sumV_R]
    ans = max(ans_lis)
    print(f'#{tc} {ans}')































