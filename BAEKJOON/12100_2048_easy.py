import sys
input = sys.stdin.readline
from copy import deepcopy
sys.setrecursionlimit(10000)


def push(line):

    numbers = []
    for number in line:
        if number:
            numbers.append(number)

    new_line = []
    i = 0
    while i < len(numbers) - 1:

        if numbers[i] == numbers[i+1]:
            new_line.append(numbers[i]*2)
            i += 1
        else:
            new_line.append(numbers[i])
        i += 1
    
    if i == len(numbers)-1:
        new_line.append(numbers[i])

    new_line += [0] * (N-len(new_line))

    return new_line


def play(lst):

    temp = deepcopy(table)

    for d in lst:
        if d == 0:
            for i in range(N):
                new_line = push(reversed(temp[i]))
                temp[i] = list(reversed(new_line))
        elif d == 1:
            for i in range(N):
                new_line = [temp[x][i] for x in range(N-1, -1, -1)]
                new_line = list(reversed(push(new_line)))
                for x in range(N):
                    temp[x][i] = new_line[x]
        elif d == 2:
            for i in range(N):
                temp[i] = push(temp[i])
        else:
            for i in range(N):
                new_line = [temp[x][i] for x in range(N)]
                new_line = push(new_line)
                for x in range(N):
                    temp[x][i] = new_line[x]

    return max([max(line) for line in temp])


def dfs(lst):

    if len(lst) == 5:
        return play(lst)

    max_v = 0
    for d in range(4):
        max_v = max(max_v, dfs(lst+[d]))
    
    return max_v


N = int(input())

table = [list(map(int, input().split())) for _ in range(N)]

print(dfs([]))

'''

dfs 함수로 4**5번 밀어줌
move1~move4 함수에서 1차원 리스트로 push 함수로 보냄
push 함수에서 작업을 마친 후 move로 반환
move에서 push로부터 반환받은대로 수정하고 dfs로 2차원 리스트 반환

5번 밀어진 케이스에서 max값 찾아서 비교 후 변수 수정
틀렸다고 나오는데 미는부분이 어딘가 잘못 만들어진듯?

'''

'''
3
2 2 2
4 4 4
8 8 8

4
0 4 0 4
4 0 4 0
0 4 0 4
4 0 4 0



'''