# NN = int(input())
# #
# def isPelindrome(s):
#     # s = s.rstrip()
#     lenS = NN
#     for idx in range(lenS//2):
#         if s[idx] != s[lenS-1-idx]:
#             return 0
#     return 1


# def check(N, M):
#     for row in range(N):
#         for st1 in range(N-M+1):
#             temp = ''
#             for col in range(M):
#                 temp += arr[row][st1+col]
#             if isPelindrome(temp):
#                 # res = temp
#                 return temp
#
#
#     for col in range(N):
#         for st2 in range(N-M+1):
#             temp = ''
#             for row in range(M):
#                 temp += arr[st2+row][col]
#             if isPelindrome(temp):
#                 # res = temp
#                 return temp

# TC = int(input())
# for tc in range(1, TC+1):

# M = int(input())
arr = [list(map(int, input().split())) for _ in range(8)]
# print(arr)

print(arr)


