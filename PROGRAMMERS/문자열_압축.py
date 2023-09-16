def solution(s):
    
    
    def slice(string, n):
        
        lst = []
        temp = 0
        p = ''
        for i in range(len(string)):
            p = p+string[i]
            temp += 1
            if temp == n:
                temp = 0
                lst.append(p)
                p = ''
        if p:
            lst.append(p)
        
        word = ''
        cnt = 1
        for i in range(1, len(lst)):
            
            if lst[i] == lst[i-1]:
                cnt += 1
                
            else:
                if cnt == 1:
                    word = word + lst[i-1]
                else:
                    word = word + str(cnt) + lst[i-1]
                    cnt = 1
            
            if i == len(lst)-1:
                if cnt == 1:
                    word = word + lst[i]
                else:
                    word = word + str(cnt) + lst[i]
        
        return len(word)
    
    
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        answer = min(answer, slice(string, i))
    
    return answer