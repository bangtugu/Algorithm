import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500) # N <= 2000이므로 모두 일렬로 이어졌다고 가정할때 dfs 함수 재귀가 2000번까지 들어갈 수 있음.

N, Q = map(int, input().split())

table = [[] for _ in range(N+1)]
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(lst[0]):
        table[i+1].append(lst[j+1])

# 전부 열렸을때 기준 순서도 구하기(dfs)
# 폴더가 열렸는지 안열렸는지 확인할 수 있는 배열 만들기(is_toggle)
# 폴더로 이동이 가능한지 확인하는 배열(can_move)
# 토글될때 하위 폴더들 순회하며 노출될지 안될지 변경하는 함수 (toggle(i))
# can_move 따라서 move 후 print

folder = []


def dfs(n):
    for i in table[n]:
        folder.append(i)
        dfs(i)


dfs(1)


def toggle(i):

    lst = table[i][:]
    idx = 0
    while idx < len(lst):
        now = lst[idx]
        can_move[now] = is_toggle[i]
        if is_toggle[now]:
            lst.extend(table[now])
        idx += 1


can_move = [0]*(N+1)
is_toggle = [0]*(N+1)
for i in table[1]:
    can_move[i] = 1
pointer = 0
orders = [input().split() for _ in range(Q)]
for order in orders:
    temp = order
    if len(temp) == 1:
        is_toggle[folder[pointer]] = 0 if is_toggle[folder[pointer]] else 1
        toggle(folder[pointer])
        
    else:
        d = -1 if int(temp[1]) < 0 else 1
        cnt = abs(int(temp[1]))
        next = pointer
        while cnt > 0:
            next += d
            if next < 0 or next >= len(folder):
                next = pointer
                break
            if can_move[folder[next]]:
                pointer = next
                cnt -= 1

        print(folder[pointer])
