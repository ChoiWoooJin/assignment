# # # TC = int(input())
# #
# def search(s):
#     num_dic = {'0001101':'0', '0011001':'1', '0010011':'2', '0111101':'3','0100011':'4', '0110001':'5', '0101111':'6', '0111011':'7','0110111':'8', '0001011':'9'}
#
#     return num_dic[s]
#
# N, M = list(map(int, input().split()))
#
# arr = [input() for _ in range(N)]
#
#
#         if arr[row][] == 1:
#             s_row = row
#             s_col = col
#
#             break
#
# print(arr[s_row][s_col+56])


# lis4 = []
# for r in lis3:
#     if r == '0001101' or r == '0011001' or r == '0010011' or r == '0111101' or r == '0100011' or r == '0110001' or r == '0101111' or r == '0111011' or r == '0110111' or r == '0001011':
#         lis4.append(search(r))
#
# print(lis4)










###########################################################################################

import sys
sys.stdin = open('input.txt', 'r')

# 7가지의 문자열을 받아서 문자코드를 return
def getCode(s):
    num_dic = {'0001101': 0, '0011001': 1,
               '0010011': 2, '0111101': 3,
               '0100011': 4, '0110001': 5,
               '0101111': 6, '0111011': 7,
               '0110111': 8, '0001011': 9}

    return num_dic[s]

TC = int(input())

for tc in range(1, TC+1):
    N, M = list(map(int, input().split()))

    arr = [input() for _ in range(N)]
    for row in range(N):
        if arr[row].count('1') > 0:
            st = M-1-arr[row][::-1].index('1') -55
            break

    # print(st)

    codes = []
    for _ in range(8):
        codes.append(getCode(arr[row][st:st+7]))
        st += 7


    sumV = 0

    for i in range(8):
        if i % 2 == 0:
            sumV += codes[i]*3
        else:
            sumV += codes[i]

    if sumV % 10:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {sum(codes)}')














