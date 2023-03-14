str='abcdefghighl'

if len(str)%2==1:
    print(str[len(str)//2])
elif len(str)%2==0:
    print(str[(len(str)-1)//2:(len(str)+2)//2])
