words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

if words[0] == 'done':
    print('done-끝')
else:
    for idx in range(1,len(words)):
        if words[idx] == 'done':
            print('done-끝')
            break
        if words[idx-1][-1] != words[idx][0] or words[idx] in words[:idx]:
            print(f'{idx} fail')
            break
    else:
        print('성공-끝')






