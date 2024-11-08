import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alps = sorted(list(input().split()))
m_lst = {'a', 'e', 'i', 'o', 'u'}
check = set()

def get_case(i, m, c, string):
    if len(string) >= L:
        if m >= 1 and c >= 2 and string not in check:
            check.add(string)
            print(string)
        return
    if i >= C: return
    if len(string) + C - i < L: return

    if alps[i] in m_lst:
        get_case(i+1, m+1, c, string+alps[i])
    else:
        get_case(i+1, m, c+1, string+alps[i])
    get_case(i+1, m, c, string)


get_case(0, 0, 0, '')