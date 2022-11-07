'''
4
1
L-
2
F+ B+
4
U- D- L+ R+
10
L- U- L+ U- L- U- U- L+ U+ U+

12
1
L-
1
L+
1
R-
1
R+
1
F+
1
F-
1
B+
1
B-
1
U+
1
U-
1
D+
1
D-
'''

dy = [0, 1, 0, -1, 1, 1, -1, -1]
dx = [1, 0, -1, 0, 1, -1, -1, 1]


def rollplat(v):

    target = cube[cube_dic[v]]

    d = 1

    y1 = x1 = y2 = 0
    x2 = 1

    temp1 = target[y1][x1]
    temp2 = target[y2][x2]

    for _ in range(3):

        target[y1][x1] = target[y1+dy[d]*2][x1+dx[d]*2]
        target[y2][x2] = target[y2+dy[d+4]][x2+dx[d+4]]

        y1 += dy[d]*2
        x1 += dx[d]*2
        y2 += dy[d+4]
        x2 += dx[d+4]

        d = (d+3)%4

    target[y1][x1] = temp1
    target[y2][x2] = temp2


def rolling(vector):

    rollplat(vector)

    '''
    
            www
            w0w
            www
         gggrrrbbb
         g4gr2rb5b
         gggrrrbbb
            yyy
            y1y
            yyy
            ooo
            o3o
            ooo
    
    '''

    if vector == 'U':
        temp = cube[2][0]
        cube[2][0] = cube[5][0]
        cube[5][0] = [cube[3][2][2], cube[3][2][1], cube[3][2][0]]
        [cube[3][2][2], cube[3][2][1], cube[3][2][0]] = cube[4][0]
        cube[4][0] = temp

    elif vector == 'D':
        temp = cube[2][2]
        cube[2][2] = cube[4][2]
        cube[4][2] = [cube[3][0][2], cube[3][0][1], cube[3][0][0]]
        [cube[3][0][2], cube[3][0][1], cube[3][0][0]] = cube[5][2]
        cube[5][2] = temp

    elif vector == 'F':
        temp = cube[0][2]
        cube[0][2] = [cube[4][2][2], cube[4][1][2], cube[4][0][2]]
        [cube[4][0][2], cube[4][1][2], cube[4][2][2]] = cube[1][0]
        cube[1][0] = [cube[5][2][0], cube[5][1][0], cube[5][0][0]]
        [cube[5][0][0], cube[5][1][0], cube[5][2][0]] = temp

    elif vector == 'B':
        temp = cube[1][2]
        cube[1][2] = [cube[4][0][0], cube[4][1][0], cube[4][2][0]]
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[0][0]
        cube[0][0] = [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
        [cube[5][2][2], cube[5][1][2], cube[5][0][2]] = temp

    elif vector == 'L':
        temp = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][0][0], cube[3][1][0], cube[3][2][0]
        cube[3][0][0], cube[3][1][0], cube[3][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = temp

    elif vector == 'R':
        temp = cube[2][0][2], cube[2][1][2], cube[2][2][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[3][0][2], cube[3][1][2], cube[3][2][2]
        cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = temp




T = int(input())

for i in range(T):

    cube_dic = {
        'U': 0,
        'D': 1,
        'F': 2,
        'B': 3,
        'L': 4,
        'R': 5
    }

    cube = [
        [['w']* 3 for _ in range(3)],
        [['y']* 3 for _ in range(3)],
        [['r']* 3 for _ in range(3)],
        [['o']* 3 for _ in range(3)],
        [['g']* 3 for _ in range(3)],
        [['b']* 3 for _ in range(3)]
    ]

    N = int(input())
    roll_d = input().split()

    print(roll_d)

    for i in range(len(roll_d)):
        cnt = 1
        print(roll_d[i][1])
        if roll_d[i][1] == '-':
            cnt = 3
        for j in range(cnt):
            rolling(roll_d[i][0])

    for line in cube[0]:
        print(*line)