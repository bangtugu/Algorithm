
string = input()

n = len(string)
maxnum = n if n <= 9 else 9+(n-9)//2
answer = []


def get(i):
    if i >= n:
        print(*answer)
        return True
    
    if string[i] != '0':

        n1 = int(string[i])
        if n1 <= maxnum and n1 not in answer:
            answer.append(n1)
            if get(i+1): return True
            answer.pop()
        
        n2 = int(string[i:i+2])
        if n2 <= maxnum and n2 not in answer:
            answer.append(n2)
            if get(i+2): return True
            answer.pop()


get(0)