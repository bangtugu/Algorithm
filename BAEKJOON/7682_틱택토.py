import sys
input = sys.stdin.readline

while True:
    line = input()

    if line[:3] == 'end': break

    table = []
    for i in range(3):
        table.append(line[3*i:3*i+3])

    Xcnt, Ocnt = 0, 0
    for i in range(3):
        for j in range(3):
            if table[i][j] == 'O':
                Ocnt += 1
            elif table[i][j] == 'X':
                Xcnt += 1
    
    if Xcnt > Ocnt+1 or Xcnt < Ocnt:
        print('invalid')
        continue
    
    Xline, Oline = [0, 0, 0], [0, 0, 0]
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2]:
            if table[i][0] == 'X': Xline[0] += 1
            elif table[i][0] == 'O': Oline[0] += 1
        if table[0][i] == table[1][i] == table[2][i]:
            if table[0][i] == 'X': Xline[1] += 1
            elif table[0][i] == 'O': Oline[1] += 1
    if table[0][0] == table[1][1] == table[2][2]:
        if table[0][0] == 'X': Xline[2] += 1
        elif table[0][0] == 'O': Oline[2] += 1
    elif table[2][0] == table[1][1] == table[0][2]:
        if table[2][0] == 'X': Xline[2] += 1
        elif table[2][0] == 'O': Oline[2] += 1
    
    if sum(Xline) and sum(Oline):
        print('invalid')
        continue

    if sum(Xline) and Xcnt == Ocnt:
        print('invalid')
        continue

    if sum(Oline) and Xcnt > Ocnt:
        print('invalid')
        continue
    
    if not sum(Xline) and not sum(Oline) and Xcnt+Ocnt < 9:
        print('invalid')
        continue

    print('valid')

'''
XOX
OXO
XO.
'''