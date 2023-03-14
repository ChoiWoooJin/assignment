\def step1(exp):
    isp = {'+': 1, '*': 2}
    ST = []
    result = []
    for i in exp:
        if i.isdigit():
            result.append(i)
        else:
            if len(ST) > 0 and isp[ST[-1]] >= isp[i]:
                result.append(ST.pop())
                ST.append(i)
            else:
                ST.append(i)
    while ST:
        result.append(ST.pop())

    return result

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    if op == '*':
        return v1 * v2

def step2(exp):
    ST =[]
    for c in exp:
        if c.isdigit():
            ST.append(int(c))
        else:
            v2 = ST.pop()
            v1 = ST.pop()
            ST.append(cal(v1, v2, c))

    return ST[-1]

TC = 10
for tc in range(1, TC+1):
    N = int(input())
    exp = input()
    post = step1(exp)

    print(f'#{tc}', step2(post))