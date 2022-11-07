N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()                                # 센서를 좌표순으로 정렬

gaps = []

for i in range(len(sensors)-1):               # 센서간 간격을 저장
    gaps.append(sensors[i+1]-sensors[i])

gaps.sort(reverse=True)                       # 간격을 내림차순으로 정렬

# print(sensors)
# print(gaps)

if len(sensors) <= K:                         # 집중국 수가 센서보다 많거나 같으면, 센서마다 하나씩 설치하면 되니까 전체합 0
    print(0)
else:                                         # (집중국 수 - 1)만큼 간격을 무시할 수 있기 때문에,
    print(sum(gaps[K-1:]))                    # (집중국 수 - 1)개만큼 무시하고 더한 값을 출력한다.