# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}


y=int(input())


import calendar
c = calendar.TextCalendar()


while calendar.isleap(y)==True:
    y=int(input('윤년입니다. 다시 입력해주세요 =>'))
print(c.formatyear(y))

y=int(input('년을 입력해주세요 : '))
m=int(input('달을 입력해주세요 : '))
d=int(input('일을 입력해주세요 : '))

if calendar.weekday(y, m, d)==0:
    print('경고 월요일입니다.')
    dic={'년': y, '월' : m, '일' : d,'요일' : '월요일'}
    print(dic)
else:
    week = {1:'화요일', 2:'수요일',3:'목요일',4:'금요일',5:'토요일',6:'일요일'}
    dic={'년': y, '월' : m, '일' : d,'요일' : week[calendar.weekday(y, m, d)] }
    print(dic)






    








    



# y=int(input())
# m=int(input())
# d=int(input())

