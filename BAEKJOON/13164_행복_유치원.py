import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
temp = [lst[i]-lst[i-1] for i in range(1, N)]
temp.sort(reverse=True)

answer = lst[-1] - lst[0] - sum(temp[:K-1])
print(answer)

'''
5 3
1 3 5 6 10
'''