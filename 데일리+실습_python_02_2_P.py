# 입력 예시
# <p>취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.</p>

# 출력 예시
# 취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.

# 방법 1
string = input()
print(string[3:-4])


# 방법 2
import re
a = input()

to_clean = re.compile('<.*?>')
cleantext = re.sub(to_clean, '',a)
print(cleantext)


