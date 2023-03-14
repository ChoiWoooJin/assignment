# TC = 10
# for tc in range(1, TC+1):

# exp = input()

def step1(exp):
    isp = {'+': 1, '*': 2, '(': 0}
    esp = {'+': 1, '*': 2, '(': 3}
    ST = []
    res =[]
    for c in exp:
        if c.isdigit():
            res.append(c)
        elif c == ')':
            while ST and ST[-1] != '(':
                res.append(ST.pop())
            ST.pop()
        else:
            if ST and isp[ST[-1]] >= esp[c]:
                res.append(ST.pop())
                ST.append(c)
            else:
                ST.append(c)
    while ST:
        res.append(ST.pop())

    return res

# print(step1(exp))

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    if op == '*':
        return v1 * v2

def step2(exp):
    ST = []
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


