def solution(cap, n, deliveries, pickups):
    
    answer = deliver = pickup = balance = 0
    
    temp = n-1
    while temp >= 0:
        
        deliver -= deliveries[temp]
        pickup -= pickups[temp]
        
        if deliver < 0:
            while deliver < 0:
                deliver += cap
                balance += 1
                if balance > 0:
                    answer += temp + 1
        
        if pickup < 0:
            while pickup < 0:
                pickup += cap
                balance -= 1
                if balance < 0:
                    answer += temp + 1
        
        temp -= 1
    
    return answer * 2