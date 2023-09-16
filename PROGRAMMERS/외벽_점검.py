# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]
# result = 2

# n = 12
# weak = [1, 3, 4, 9, 10]
# dist = [3, 5, 7]
# result = 1

n = 16
weak = [1,2,3,4,5,7,8,10,11,12,14,15]
dist = [4,2,1,1]
result = 4


def solution(n, weak, dist):

    gap = [0] * len(weak)
    for i in range(len(weak)-1):
        gap[i] = weak[i+1]-weak[i]
    gap[-1] = min(weak[-1]-weak[0], n-weak[-1]+weak[0])
    dist.sort(reverse=True)


    def check(lst, N, M, l):
        
        if N == M:
            if sum(lst) == 0:
                return True
            return False
        
        for i in range(len(weak)):
            temp = lst[:]
            temp[i] = 0
            move = dist[N]
            idx = l
            while gap[idx] <= move:
                move -= gap[idx]
                idx = (idx+1)%len(weak)
                temp[idx] = 0
            if check(temp, N+1, M, idx):
                return True

        return False


    for i in range(1, len(dist)+1):
        for j in range(len(weak)):
            if check([1]*len(weak), 0, i, j):
                return i
    return -1


def solution2(n, weak, dist):

    gap = [0] * len(weak)
    for i in range(len(weak)-1):
        gap[i] = weak[i+1]-weak[i]
    gap[-1] = min(weak[-1]-weak[0], n-weak[-1]+weak[0])
    dist.sort(reverse=True)
    

    def check(lst):
        friends = dist[:len(lst)]
        print(lst, friends)
        for z in range(len(lst)):
            if lst[z] > dist[z]:
                return False
        
        return True

    
    from itertools import combinations
    for i in range(1, len(dist)+1):
        for passing in combinations(range(len(weak)), i):
            
            temp = gap[:]
            for idx in passing:
                temp[idx] = 0
            gaps = [0] * i
            idx = 0
            for g in temp:
                if g == 0:
                    idx = (idx+1)%i
                else:
                    gaps[idx] += g
            gaps.sort(reverse=True)
            if check(gaps):
                return i
    
    return -1


print(solution2(n, weak, dist))