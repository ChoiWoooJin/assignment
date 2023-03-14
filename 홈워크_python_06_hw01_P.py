# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g
import re

lst = list()
n = 1
while n <= 5:
    temp = input()
    if temp =='Done':
        break    
    else:
        t = temp.split(' ')
        lst.append(t)
    n += 1


p_list=[]
s_list=[]
for i in lst:
    p_list.append(i[0])
    s_list.append(i[1])
    print(p_list) 
    print(s_list)

pp_list=[]
for e in p_list:
    number = re.findall(r'\d+', e)
    pp_list.append(int(number))
    print(pp_list)

ss_list=[]
for e2 in s_list:
    number2 = re.findall(r'\d+', e2)
    ss_list.append(int(number2))
    print(ss_list)


