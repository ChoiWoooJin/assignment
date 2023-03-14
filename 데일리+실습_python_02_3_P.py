str_lst = list(input('문자열을 입력하세요. : ').split())

for i in range(len(str_lst)-1):
    if str_lst[i][-1] != str_lst[i+1][0] :
        print('False')
        break
    
else:
    print('True')

    



