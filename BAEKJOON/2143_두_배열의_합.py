import sys
input = sys.stdin.readline

T = int(input())
N = int(input())
n_lst = [[0]*(N+1) for _ in range(N+1)]
n_line = list(map(int, input().split()))
M = int(input())
m_lst = [[0]*(M+1) for _ in range(M+1)]
m_line = list(map(int, input().split()))


def set_dic(Z, z_lst, z_line):
    dic = {}
    for i in range(1, Z+1):
        for j in range(i, Z+1):
            if i == j: z_lst[i][j] = z_line[i-1]
            else:
                z_lst[i][j] = z_lst[i][j-1] + z_line[j-1]
            
            if z_lst[i][j] not in dic: dic[z_lst[i][j]] = 0
            dic[z_lst[i][j]] += 1

    return dic


n_dic = set_dic(N, n_lst, n_line)
m_dic = set_dic(M, m_lst, m_line)

answer = 0
for i in sorted(n_dic.keys()):
    if T-i in m_dic:
        answer += n_dic[i] * m_dic[T-i]

print(answer)