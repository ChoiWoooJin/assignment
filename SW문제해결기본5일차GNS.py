dic = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

TC = int(input())

for tc in range(1, TC+1):

    a, num1 = input().split()
    num1 = int(num1)
    lis = list(input().split())

    nums = []
    for s in lis:
        nums.append(dic[s])

    for i in range(num1 - 1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(num1,nums)

    dic_reverse = {v:k for k,v in dic.items()}

    nums2 = []
    for u in nums:
        nums2.append(dic_reverse[u])

    print(f'#{tc}')
    print(' '.join(nums2))




