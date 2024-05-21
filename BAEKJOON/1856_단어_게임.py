import sys
input = sys.stdin.readline

'''
6 10
browndcodw
cow
milk
white
black
brown
farmer

2



10 11
broaadfcast
broad
cast
broaa
acast
bread
trace
cost
break
failed
collect

2
'''
w, l = map(int, input().split())
S = input()
words = [input().split()[0] for _ in range(w)]



# sett = set(words)
# word_dic = {'end' : 0}

# for word in words:
#     now = word_dic
#     for alp in word:
#         if alp not in now.keys(): now[alp] = {'end': 0}
#         now = now[alp]
    
#     now['end'] += 1

# answer = l

# lst = []
# lst.append([0, 0, ''])

# while lst:
#     print(lst)
#     idx, skip, string = lst.pop()
#     if skip >= answer: continue
#     if idx >= l:
#         answer = min(skip, answer) if string in sett else min(skip + len(string), answer) 
#         continue

#     if skip+1 < answer: lst.append([idx+1, skip+1, string])
    
#     now = word_dic
#     for alp in string:
#         now = now[alp]
#     if S[idx] in now.keys():
#         if now[S[idx]]['end']:
#             lst.append([idx+1, skip, ''])
#         lst.append([idx+1, skip, string+S[idx]])

# print(answer)




dp = [i for i in range(l+1)]

for i in range(l):

    for word in words:
        if word[0] == S[i] and len(word)+i <= l:
            idx ,skip = 0, 0
            can_submit = False
            while i+idx+skip < l:
                if word[idx] == S[i+idx+skip]:
                    if idx == len(word)-1:
                        can_submit = True
                        break
                    idx += 1
                else:
                    skip += 1
            
            if can_submit:
                dp[i+1+idx+skip] = min(dp[i+1+idx+skip], dp[i]+skip)

    dp[i+1] = min(dp[i+1], dp[i]+1)

print(dp[l])