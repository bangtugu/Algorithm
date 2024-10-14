import sys
input = sys.stdin.readline

N = int(input())
root_dic = {}

for _ in range(N):
    line = input().split()

    for i in range(1, int(line[0])+1):
        if i == 1:
            p = root_dic
        else:
            p = p[line[i-1]]

        if line[i] not in p:
            p[line[i]] = {}


def dfs(dic, n):
    if not dic:
        return
    
    for key in sorted(dic.keys()):
        print('--'*n+key)
        dfs(dic[key], n+1)


dfs(root_dic, 0)