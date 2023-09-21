import clipboard


lines = clipboard.paste()
lines = lines.split('\n')

while True:
    for i in range(len(lines)):
        if lines[i] == '' or lines[i] == '\r':
            lines.remove(lines[i])
            break
    else:
        break


ex = ''
if lines:
    N = len(lines)
    title = lines[0].split()
    for i in range(1, N):
        if lines[i]:
            line = lines[i].split('\t')
            for j in range(len(title)):
                cnt = 0
                ex += '{} = {}\n'.format(title[j], line[j])
        ex += '\n'
print(ex)
clipboard.copy(ex)
