a,b,c =list(map(int,input().split()))
if a==b and b==c and a==c:
    print('정삼각형')
elif a+b<=c or a+c<=b or b+c<=a:
    print('삼각형 아님')
else:
    if a==b or b==c or a==c:
        print('이등변삼각형')
    elif (a**2)+(b**2)==c**2:
        print('직각삼각형')
    else:
        print('삼각형')


        
        
        
