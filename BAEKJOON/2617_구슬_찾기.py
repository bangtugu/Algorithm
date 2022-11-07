'''

    N은 항상 홀수이다.
    어떠한 공이 중간 무게가 될 가능성이 없어지려면,
    해당 공보다 확실히 무거운 공이 (N-1)/2 개보다 많거나, 확실히 가벼운 공이 (N-1)/2개보다 많아야 한다.
    만약 조건에 해당하지 않는다면, 중간값일 가능성이 있다.

    주어지는 데이터는 '(더 무거운 공 번호) (더 가벼운 공 번호)' 형식으로 주어지므로,
    (인덱스 0은 배제시키기 위해) N+1개의 빈 리스트를 갖는 리스트를 2개 생성하여,
    인덱스값의 공보다 가벼운 공 리스트를 저장 / 무거운 공 리스트를 저장하는 리스트를 저장하여 두 트리 구조를 생성한다.
    그리고 두 트리에서 자식 노드의 수가 (N-1)/2개보다 많은 인덱스는 곧 위 문단의 조건에 해당한다고 볼 수 있다.

'''


# def getchild(lst, start, now, n):
#
#     if n == N // 2:
#         if start not in cannot:
#             cannot.append(start)
#         return
#
#     for num in lst[now]:
#         if not v[num]:
#             v[num] = 1
#             getchild(lst, start, num, n+1)
#             v[num] = 0
#             if start in cannot:
#                 return


from collections import deque


def check(lst, n):
    Q = deque()
    Q.extend(lst[n])

    child = []                          # 자식 노드(더 무겁거나 가벼운 공들) 리스트

    while Q:
        now = Q.popleft()
        if now not in child:
            child.append(now)
            if len(child) > N // 2:     # 자식 노드의 숫자가 N//2를 초과할 경우 즉시 1을 리턴한다.
                return 1
            Q.extend(lst[now])

    return 0                            # 자식 노드의 숫자가 N//2 이하일 경우 0을 리턴한다.


N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
r_tree = [[] for _ in range(N+1)]

for i in range(M):
    h, l = map(int, input().split())
    tree[h].append(l)                   # 인덱스 안의 리스트 = 인덱스값보다 가벼운 애들
    r_tree[l].append(h)                 # 인덱스 안의 리스트 = 인덱스값보다 무거운 애들

cnt = 0                                 # 중간 무게일 가능성이 없는 공의 숫자

for i in range(1, N+1):
    result = check(tree, i)             # i번 공보다 가벼운 공이 N//2개 초과로 존재하는지 확인
    if not result:
        result = check(r_tree, i)       # 아니라면 무거운 공이 N//2개 초과로 존재하는지
    cnt += result

print(cnt)



# 시간초과
# from collections import deque
#
#
# def calc(lst):
#
#     childs = [[] for _ in range(N + 1)] # 자식 노드들을 저장할 리스트
#
#     for i in range(1, N + 1):           # 인덱스보다 가볍거나 무거운 애들 찾기
#         Q = deque()
#         Q.extend(lst[i])
#         while Q:
#             n = Q.popleft()
#             if n not in childs:
#                 childs[i].append(n)
#                 Q.extend(lst[n])
#
#     cnt = 0
#     for i in range(1, N + 1):
#         if len(childs[i]) > N // 2:
#             cnt += 1
#
#     return cnt
#
#
# N, M = map(int, input().split())
# tree = [[] for _ in range(N+1)]
# r_tree = [[] for _ in range(N+1)]
#
# for i in range(M):
#     h, l = map(int, input().split())
#     tree[h].append(l)                   # 인덱스 안의 리스트 = 인덱스값보다 가벼운 애들
#     r_tree[l].append(h)                 # 인덱스 안의 리스트 = 인덱스값보다 무거운 애들
#
# result = calc(tree) + calc(r_tree)
#
# print(result)


# 함수로 바꾸기 전
# childs = [[] for _ in range(N + 1)]     # 해당 인덱스의 자식 노드들을 저장하는 리스트
#
# for i in range(1, N+1):                 # 인덱스보다 가벼운 애들 찾기
#     Q = deque()
#     Q.extend(tree[i])
#     while Q:
#         n = Q.popleft()
#         if n not in childs:
#             childs[i].append(n)
#             Q.extend(tree[n])
#
# for i in range(1, N+1):
#     if len(childs[i]) > N//2:
#         iscannot.append(i)
#
# childs = [[] for _ in range(N + 1)]
#
# for i in range(1, N+1):                 # 인덱스보다 무거운 애들 찾기
#     Q = deque()
#     Q.extend(r_tree[i])
#     while Q:
#         n = Q.popleft()
#         if n not in childs:
#             childs[i].append(n)
#             Q.extend(r_tree[n])
#
# for i in range(1, N+1):
#     if len(childs[i]) > N//2:
#         iscannot.append(i)


