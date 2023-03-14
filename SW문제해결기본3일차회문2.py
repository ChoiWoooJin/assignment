def isPelindrome(s):
    # s = s.rstrip()
    lenS = 0
    for _ in s:
        lenS += 1
    for idx in range(lenS//2):
        if s[idx] != s[lenS-1-idx]:
            return 0
    return 1


def check(N):
    for row in range(N):

        temp = ''
        for col in range(N):
            temp += arr[row][col]
        if isPelindrome(temp):
            # res = temp
            return temp


    for col in range(N):

        temp = ''
        for row in range(N):
            temp += arr[row][col]
        if isPelindrome(temp):
            # res = temp
            return temp


# TC = int(input())
# for tc in range(1, TC+1):
N = 100

arr = input()
print(check(100))



