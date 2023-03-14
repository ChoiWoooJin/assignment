entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']


from collections import Counter

# 가장 많이 입장한 세 사람
entry=Counter(entry_record)
entry_top3 = entry.most_common(3)
print(f'입장 기록이 많은 Top3 \n{entry_top3[0][0]} {entry_top3[0][1]}회\n{entry_top3[1][0]} {entry_top3[1][1]}회\n{entry_top3[2][0]} {entry_top3[2][1]}회')

# 입장 횟수와 퇴장 횟수가 같지 않은 사람
exit=Counter(exit_record)
entry.subtract(exit)
entry=list(entry.items())


a=[]
for i in range(len(entry)):
    if entry[i][1] != 0:
        a.append(entry[i])


print('출입 기록이 수상한 사람')
for s in a:
    if s[1]<0:
        print(f'{s[0]}은 퇴장기록이 {abs(s[1])}회 더 많아 수상합니다.')
    elif s[1]>0:
        print(f'{s[0]}은 입장기록이 {s[1]}회 더 많아 수상합니다.')

###########################################################################################################3

# from collections import Counter

# entry_counter = Counter(entry_record)
# exit_counter = Counter(exit_record)
# new_lst = sorted(entry_counter.items(), key = lambda x : x[1], reverse=True)

# #가장 많이 입장한 세 사람
# rlt = new_lst[:3]
# print('입장 기록 많은 Top3')
# for i in range(len(rlt)):
#     name = rlt[i][0]
#     en_cnt = rlt[i][1]
#     print(f'{name} {en_cnt}회')

# #입장 횟수와 퇴장 횟수가 같지 않은 사람
# print()
# print('출입 기록이 수상한 사람')
# en_lst = sorted(entry_counter.items(), key = lambda x: x, reverse=True)
# ex_lst = sorted(exit_counter.items(), key = lambda x: x, reverse=True)

# for i in range(len(ex_lst)):
#     a = ex_lst[i]
#     b = en_lst[i]
#     cnt = abs(a[1] - b[1])
#     if a[1] > b[1]:
#         print(f'{a[0]}은 퇴장기록이 {cnt}회 더많아 수상합니다.')
#     elif a[1] < b[1]:
#         print(f'{a[0]}은 입장기록이 {cnt}회 더많아 수상합니다.')













