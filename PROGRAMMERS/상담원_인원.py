# k = 3
# n = 5
# reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]
# result = 25

k = 2
n = 3
reqs = [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]
result = 90


def solution(k, n, reqs):
    s = [[] for _ in range(k+1)]
    t = [[] for _ in range(k+1)]
    left = n - k

    for a, b, c in reqs:
        s[c].append(a)
        t[c].append(b)


    def check(case, man):
        cnt = 0
        wait = 0
        e = []
        start = end = 0

        while True:
            if start >= len(s[case]):
                break
            if end >= len(e):
                e.append(s[case][start] + t[case][start])
                e.sort()
                cnt += 1
                start += 1
                continue

            if s[case][start] < e[end]:
                if cnt < man:
                    e.append(s[case][start] + t[case][start])
                    e.sort()
                    cnt += 1
                    start += 1
                else:
                    e.append(e[end] + t[case][start])
                    e.sort()
                    wait += e[end] - s[case][start]
                    start += 1
                    end += 1
            elif s[case][start] == e[end]:
                e.append(s[case][start] + t[case][start])
                e.sort()    
                start += 1
                end += 1
            else:
                cnt -= 1
                end += 1

        
        return wait
    

    lst = [[0] * (left+2) for _ in range(k+1)]

    for i in range(1, k+1):
        for j in range(1, left+2):
            lst[i][j] = check(i, j)
            if lst[i][j] == 0:
                break
    

    def check(n, left, numbers, min_wait):
        if n >= k-1:
            numbers[n] += left
            wait = 0
            for i in range(k):
                wait += lst[i+1][numbers[i]]
            numbers[n] -= left
            return min(min_wait, wait)
        
        for i in range(left+1):
            numbers[n] += i
            min_wait = min(min_wait, check(n+1, left-i, numbers, min_wait))
            numbers[n] -= i

        return min_wait

    
    numbers = [1] * k
    min_wait = check(0, left, numbers, 9999999999)
    return min_wait


print(solution(k, n, reqs))