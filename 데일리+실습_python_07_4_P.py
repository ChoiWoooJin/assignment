# fee(600, 50) #=> 91000
# fee(600, 110) #=> 10

def fee(a,b):
    rent = (a/10)*1200
    if a%30 >= 20 and a%30 <= 29:
        insurance = ((a//30)+1)*525
    else:
        insurance = (a//30)*525
    if b>=100:
        drive = (170*100)+(85*(b-100))
    else:
        drive = 170*b
    return rent + insurance + drive
    
print(fee(600, 50)) #=> 91000
print(fee(600, 110)) #=> 10





