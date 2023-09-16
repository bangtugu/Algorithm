key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1]]
result = True


def solution(key, lock):
    
    L = len(lock)
    K = len(key)
    T = L+2*K

    l = [[0] * T for _ in range(T)]

    for i in range(L):
        for j in range(L):
            l[K+i][K+j] = lock[i][j]

    
    def turn(k):

        new_k = []

        for i in range(K):
            temp = []
            for j in range(K-1, -1, -1):
                temp.append(k[j][i])
            
            new_k.append(temp)

        return new_k


    def check(k, y, x):
        
        l = [[0] * T for _ in range(T)]

        for i in range(K):
            for j in range(K):
                l[y+i][x+j] += k[i][j]
        
        for i in range(L):
            for j in range(L):
                if l[K+i][K+j]+lock[i][j] != 1:
                    return False

        return True


    def solve(k):

        n = 0
        while True:

            for i in range(1, L+K):
                for j in range(1, L+K):
                    if check(k, i, j):
                        return True
            
            if n >= 3:
                break
            n += 1

            k = turn(k)
        
        return False

    
    return solve(key)


def solution2(key, lock):
    
    L = len(lock)
    K = len(key)
    

    def turn(k):

        new_k = []

        for i in range(K):
            temp = []
            for j in range(K-1, -1, -1):
                temp.append(k[j][i])
            
            new_k.append(temp)

        return new_k


    def check(k, y, x):

        for i in range(L):
            for j in range(L):
                if i-y < 0 or j-x < 0 or i-y >= K or j-x >= K:
                    if not lock[i][j]:
                        return False
                elif lock[i][j] == k[i-y][j-x]:
                    return False
                
        return True


    def solve(k):

        n = 0
        while True:

            for i in range(1-K, L):
                for j in range(1-K, L):
                    if check(k, i, j):
                        return True
            
            if n >= 3:
                break
            n += 1

            k = turn(k)
        
        return False

    
    return solve(key)


print(solution2(key, lock))