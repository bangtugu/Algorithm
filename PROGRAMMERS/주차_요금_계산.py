fees, records, result = [180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"], [14600, 34400, 5000]
# fees, records, result = [120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"], [0, 591]
# fees, records, result = [1, 461, 1, 10], ["00:00 1234 IN"], [14841]


def solution(fees, records):
    freetime, standard_fee, time_per, time_fee = fees
    park = {}
    time_dic = {}

    for record in records:
        time, carnum, status = record.split()
        time = list(map(int, time.split(':')))
        
        if carnum not in time_dic.keys():
            time_dic[carnum] = 0
        
        if status == 'IN':
            park[carnum] = time
        else:
            time_dic[carnum] += (time[0] - park[carnum][0]) * 60 + time[1] - park[carnum][1]
            park.pop(carnum)

    for carnum in park.keys():
        time = [23, 59]
        time_dic[carnum] += (time[0] - park[carnum][0]) * 60 + time[1] - park[carnum][1]
    
    answer = []
    for num in sorted(list(time_dic.keys())):
        fee = standard_fee
        time = time_dic[num]
        if time > freetime:
            time -= freetime
            fee += time//time_per * time_fee
            if time % time_per:
                fee += time_fee
        answer.append(fee)
    
    return answer


print(solution(fees, records))