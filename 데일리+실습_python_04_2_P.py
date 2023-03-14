students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

a = set(students) # set로 유니크 값 확인
print(a)
b = {'강디티': students.count('강디티'),'김철수': students.count('김철수'),'이영희':students.count('이영희'),
'조민지':students.count('조민지'),'김해킹': students.count('김해킹'),'박해피': students.count('박해피'), '한케이': students.count('한케이')}
b_sorted = sorted(b.items(), key = lambda x : x[1], reverse = True) # 딕셔너리 자체로 정렬 불가 리스트로 바꿔서 정렬해주기 그 과정에서 람다 사용, x[0]하면 키로 정렬 x[1]은 벨류로 정렬
print(b_sorted)

# 리스트 안에 있는 튜플, 딕셔너리도 마찬가지임 (리스트로 바꿔줄 필요 없음) (sort이용)

# ex) persons = [{'name':'Tom', 'age':20},{'name':'Jane', 'age':30},{'name':'Bill', 'age':25}]
# persons.sort(key = lambda x : x['age'], reverse=True)
# print(persons)