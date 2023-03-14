# TC = 10
# for tc in range(1, TC+1):
#
#     N, s = list(map(int, input().split()))
#
#     stack= []
#     for i in str(s):
#         if stack != [] and stack[-1] == i:
#             stack.pop(-1)
#         else:
#             stack.append(i)
#
#     stack = ''.join(map(str, stack))
#
#
#     print(f"#{tc} {stack.lstrip('0')}")


######################################################

#
TC = 10
for tc in range(1, 11):

    N, arr = list(input().split())
    N = int(N)


    lis = list(map(int, arr))



    ST = []
    for i in range(N):

        if ST and ST[-1] == lis[i]:
            ST.pop(-1)

        else:
            ST.append(lis[i])

    ST = ''.join(map(str, ST))

    print(f'#{tc} {ST.lstrip("0")}')
























