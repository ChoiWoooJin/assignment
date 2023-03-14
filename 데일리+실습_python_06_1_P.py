# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(num):
    newnum = num.replace('-','')
    newnum = newnum.replace(newnum[6:],'*'*len(newnum[6:]))
    return newnum

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))

