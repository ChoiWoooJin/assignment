answer = 12345
sum=0
while sum<3:
    a = int(input())
    if a == answer:
        break
    elif a != answer:
        print('비밀번호가 틀렸습니다.')
        sum = sum + 1