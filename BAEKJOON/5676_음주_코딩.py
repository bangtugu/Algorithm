import sys
input = sys.stdin.readline
sys.setrecursionlimit(1500)


def create(l, r, i):
    if l == r:
        tree[i][lst[l-1]] += 1
        return tree[i]

    m = (l+r)//2
    left = [0, 0, 0]
    right = [0, 0, 0]
    left = create(l, m, i*2)
    right = create(m+1, r, i*2+1)
    for j in range(3):
        tree[i][j] += left[j] + right[j]
    return tree[i]


def update(l, r, i):
    if l <= x <= r:
        tree[i][lst[x-1]] -= 1
        tree[i][y] += 1

    if l == r: return

    m = (l+r)//2
    if l <= x <= m:
        update(l, m, i*2)
    else:
        update(m+1, r, i*2+1)


def get(l, r, i):
    if x <= l and r <= y:
        return tree[i]

    left = [0, 0, 0]
    right = [0, 0, 0]
    now = [0, 0, 0]
    m = (l+r)//2
    if x <= m:
        left = get(l, m, i*2)
    if m+1 <= y:
        right = get(m+1, r, i*2+1)
    for j in range(3):
        now[j] += left[j] + right[j]
    return now


while True:
    try:
        N, K = map(int, input().split())
        lst = list(map(int, input().split()))
        for i in range(N):
            if lst[i] > 0:
                lst[i] = 1
            elif lst[i] < 0:
                lst[i] = 2
        
        tree = [[0, 0, 0] for _ in range(N*4)]
        create(1, N, 1)

        answer = ''
        for _ in range(K):
            M, x, y = input().split()
            x, y = int(x), int(y)
            if M == 'C':
                if y > 0:
                    y = 1
                elif y < 0:
                    y = 2
                if lst[x-1] != y:
                    update(1, N, 1)
                    lst[x-1] = y
            else:
                temp = get(1, N, 1)
                if temp[0]:
                    answer += '0'
                elif temp[2]%2:
                    answer += '-'
                else:
                    answer += '+'
        
        print(answer)
    except Exception:
        break


'''
4 6
-2 6 0 -1
C 1 10
P 1 4
C 3 7
P 2 2
C 4 -5
P 1 4
5 9
1 5 -2 4 3
P 1 2
P 1 5
C 4 -5
P 1 5
P 4 5
C 3 0
P 1 5
C 4 -5
C 4 -5

0+-
+-+-0
'''