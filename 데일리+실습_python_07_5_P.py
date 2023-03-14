import random

class ClassHelper:
    def __init__(self,name):
        self.name = name
        
    
    def pick(self,n):
        lis=[]
        for i in range(1,n+1):
            lis.append(random.choice(self.name))
        return lis

    # def match_pair(self):

ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])



print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

# print(ch.match_pair())




