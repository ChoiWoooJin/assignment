# A.    입력 예시 
#eat tea tan ate nat bat

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 
# lst = list(input().split())
# s_list=[]
# def group_anagrams(a):
#     for i in lst:
#         si=sorted(i)
#         s_list.append(si)
#     for s in range(len(s_list)):
#         if s == s[0:7]:


# print(group_anagrams(lst))

#   # words = input().split(" ")
# words = "eat tea tan ate nat bat".split(" ")

# def group_anagrams(words):
#     wordSplit = []
#     # 일단 문자를 다 쪼개서 리스트로 만든 후 정렬 후 다시 합쳐서 새로운 리스트에 저장
#     for i in range(len(words)):
#         wordSplit.append("".join(sorted(list(words[i]))))
#     # 집합을 이용해 중복을 제거한 후 다시 리스트로 변환 -> 쓰기 더 편하니까
#     wordList = list(set(wordSplit))
#     # 반환할 리스트 안에 리스트 미리 만들어주기 -> 개수는 len(wordList)
#     anagrams = []
#     for i in range(len(wordList)):
#         anagrams.append([])
#     # 
#     for i in range(len(wordSplit)):
#         for k in range(len(wordList)):
#             if wordSplit[i] == wordList[k]:
#                 anagrams[k].append(words[i])
    
#     return anagrams

# print(group_anagrams(words))


#########################################
def getSortedStr(strValue):
    t=sorted(strValue)
    t= ''.join(t)
    return t

inputL = input().split()
res ={} 


for strV in inputL:
    sortedV=getSortedStr(strV)
    if sortedV in res.keys():
        res[sortedV].append(strV)
    else:
        res[sortedV] = [strV]

print(list(res.values()))

