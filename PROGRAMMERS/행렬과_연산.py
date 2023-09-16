# rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# operations = ["Rotate", "ShiftRow"]
# result = [[8, 9, 6], [4, 1, 2], [7, 5, 3]]

# rc = [[8, 6, 3], [3, 3, 7], [8, 4, 9]]
# operations = ["Rotate", "ShiftRow", "ShiftRow"]
# result = [[8, 3, 3], [4, 9, 7], [3, 8, 6]]

rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
result = [[1, 6, 7 ,8], [5, 9, 10, 4], [2, 3, 12, 11]]

'''
1
'''
def solution1(rc, operations):

    N = len(rc)
    M = len(rc[0])


    def shiftrow(temp_rc, n):
        n = n % N
        temp_rc = temp_rc[-n:] + temp_rc[:-n]

        return temp_rc


    def rotate(temp_rc, n):
        outside = N*2 + M*2 - 4
        temp = [0] * outside

        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        
        n = n % outside
        d = 0
        y = x = 0
        for i in range(outside):
            temp[i] = temp_rc[y][x]
            
            yy = y + dy[d]
            xx = x + dx[d]

            if 0 <= yy < N and 0 <= xx < M:
                y = yy
                x = xx
            else:
                d = (d + 1) % 4
                y += dy[d]
                x += dx[d]

        d = 0
        y = x = 0
        for i in range(outside):
            temp_rc[y][x] = temp[n]
            
            n += 1
            if n >= outside:
                n = 0
                
            yy = y + dy[d]
            xx = x + dx[d]

            if 0 <= yy < N and 0 <= xx < M:
                y = yy
                x = xx
            else:
                d = (d + 1) % 4
                y += dy[d]
                x += dx[d]
        
        return temp_rc
    
    
    now = "Rotate"
    cnt = 0
    for operation in operations:
        
        if now != operation:

            if now == "Rotate":
                rc = rotate(rc, cnt)
            else:
                rc = shiftrow(rc, cnt)

            now = operation
            cnt = 1
        
        else:
            cnt += 1

    if now == "Rotate":
        rc = rotate(rc, cnt)
    else:
        rc = shiftrow(rc, cnt)

    return rc

'''
효율성 테스트에서 3tc 시간초과

연속된 rotate, shiftrow를 한번에 처리하게 했다.
하지만 rotate와 shiftrow가 번갈아서 한번씩 나오면 결국 의미가 없으니
deque를 사용해서 rotate, shiftrow 함수 자체의 속도를 빠르게 해야겠다.
'''

'''
2
'''
def solution2(rc, operations):
    from collections import deque
    
    left = deque()
    right = deque()
    body = deque()

    for i in range(len(rc)):
        left.appendleft(rc[i][0])
        right.append(rc[i][-1])
        body.append(deque(rc[i][1:-1]))

    for operation in operations:
        if operation == "Rotate":
            body[0].appendleft(left.pop())
            right.appendleft(body[0].pop())
            body[-1].append(right.pop())
            left.appendleft(body[-1].popleft())
        else:
            body.appendleft(body.pop())
            right.appendleft(right.pop())
            left.append(left.popleft())

    for i in range(len(left)):
        body[i].append(right.popleft())
        body[i].appendleft(left.pop())
        rc[i] = list(body[i])

    return rc


print(solution2(rc, operations))