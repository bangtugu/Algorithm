print(ord('z'))

print(ord('A'))

string = ''
for num in range(ord('A'), ord('z')+1):
    string = string + str(num) + chr(num) + ' '

print(string)

print(15**5 - (13**5+13**5+12**5) + (12**5+10**5+10**5) - 9**5)