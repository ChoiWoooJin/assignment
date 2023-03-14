# # TC = 10
# # for tc in range(1, TC+1):
#
# N = int(input())
# tree = [0] * (N+1)
# for _ in range(N):
#     N, *V = list(input().split())
#     N = int(N)
#     tree[N] = V[0]
#     # print(V)
# print(tree)
#
#
#
# def postorder(i):
#     if i:
#         postorder(left[i])
#         postorder(right[i])
#         print(i, end= ' ')
#
#     return
#
#
# postorder(1)

#################################################
def process(v1, v2, op):
    if op == '+':
        return v1+v2
    if op == '-':
        return v1-v2
    if op == '*':
        return v1*v2
    if op == '/':
        return v1//v2


def postorder(root):
    v = TREE[root][0]
    if v.isdigit():
        return int(v)

    else:
        lvalue = postorder(int(TREE[root][1]))
        rvalue = postorder(int(TREE[root][2]))
        res = process(lvalue, rvalue, TREE[root][0])

        return res

TC = 10
for tc in range(1, TC+1):
    N = int(input())
    TREE = [[] for _ in range(N + 1)]

    for i in range(N):
        inp = input().split()
        idx = int(inp[0])
        TREE[idx] = inp[1:]

    print(f'#{tc}', postorder(1))


