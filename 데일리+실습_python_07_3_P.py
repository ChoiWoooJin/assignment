# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        print(f'{self.a + self.b}')
              
    def sub(self):
        print(f'{self.a - self.b}')
    
    def mul(self):
        print(f'{self.a * self.b}')

    def div(self):
        if self.b == 0:
            print('0으로 나눌 수 없습니다.')
        else:
            print(f'{self.a / self.b}')

answer = Calculator(1,2)
answer.add()
answer = Calculator(2,1)
answer.sub()
answer = Calculator(3,4)
answer.mul()
answer = Calculator(4,0)
answer.div()




    
    
    
