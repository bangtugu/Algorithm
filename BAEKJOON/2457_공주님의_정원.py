import sys
input = sys.stdin.readline
# sys.setrecursionlimit(1000) # 재귀시 사용

m_dic = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
S = 1
temp = 60
E = 334
N = int(input())
fllowers = [0]*366
for i in range(N):
    sm, sd, em, ed = map(int, input().split())
    s = sum([m_dic[i] for i in range(1, sm)]) + sd
    e = sum([m_dic[i] for i in range(1, em)]) + ed
    fllowers[s] = max(fllowers[s], e)

answer = 0
while temp <= E:
    max_d = 0
    for i in range(S, temp+1):
        max_d = max(fllowers[i], max_d)
    
    S = temp
    temp = max_d
    if not temp: break
    answer += 1

if temp < E:
    print(0)
else:
    print(answer)