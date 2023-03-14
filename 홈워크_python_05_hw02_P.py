# fn_d(91) 
# 출력 예시 
# 101

def fn_d(n):
    num_list = list(map(int, str(n)))
    return sum(num_list)+n


def is_selfnumber(i):
    while n<100:
        if i != fn_d(n):
            return '셀프 넘버 입니다.'
        elif i == fn_d(n):
            return '셀프 넘버가 아닙니다.'
    
is_selfnumber(3)


    



    

        



    

    
    

    
