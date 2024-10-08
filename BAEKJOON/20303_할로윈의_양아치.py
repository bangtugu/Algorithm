import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
candy = [0] + list(map(int, input().split()))
group = list(range(N+1))


def leader(n):
    if group[n] != n:
        group[n] = leader(group[n])
    return group[n]


for _ in range(M):
    a, b = map(int, input().split())
    A = leader(a)
    B = leader(b)
    if A < B:
        group[B] = A
    else:
        group[A] = B

for i in range(1, N+1):
    L = leader(i)

leader_set = set()
cnt = [0]*(N+1)
for i in range(1, N+1):
    cnt[group[i]] += 1
    if group[i] != i:
        candy[group[i]] += candy[i]
    leader_set.add(group[i])

dp = [0]*K
for i in list(leader_set):
    for j in range(K-1, cnt[i]-1, -1):
        dp[j] = max(dp[j], dp[j-cnt[i]] + candy[i])

print(max(dp))

'''
pypy3으로 통과
python3 통과한 제출이 하나도 없음;;
'''