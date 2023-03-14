orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

menu = list(orders.split(','))

ice = [ ]
for i in menu:
    if '아이스' in i:
        ice.append(i)

print(len(ice))


counter = {}
for value in menu:
    if value in counter:
        counter[value] += 1
    else:
        counter[value] = 1
print(counter)