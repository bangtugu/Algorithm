import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000)

'''
5 5
.xx..
..x..
.....
...x.
...x.

6 10
..x.......
.....x....
.x....x...
...x...xx.
..........
....x.....

'''

N, M = map(int, input().split())

table = [[0]*M for _ in range(N)]
road = [input() for _ in range(N)]
dy = [-1, 0, 1]


def dfs(y, x):
    if x == M-1:
        return 1

    for d in range(3):
        yy = y + dy[d]
        xx = x + 1
        
        if yy < 0 or xx < 0 or yy >= N or xx >= M or table[yy][xx] or road[yy][xx] == 'x': continue

        table[yy][xx] = 1
        if dfs(yy, xx): return 1
        # table[yy][xx] = 0
        # 0으로 초기화시키면 같은 실패경우를 반복하게 되어 시간초과에 걸리게 된다.
        # 이전 재귀에서 이미 실패하여 돌아온 경우이기 때문에, 같은 파이프의 다른 경로에서 중복되든, 다른 파이프이든 여기를 지나는 파이프는 결국 실패할 경로이다. 

    return 0


answer = 0
for i in range(N):
    answer += dfs(i, 0)
print(answer)