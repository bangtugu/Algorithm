n = int(input())

wine_list = [0]*(n+1)

for i in range(n):
    wine_list[i] = int(input())

drink = [0]*(n+1)

drink[0] = wine_list[0]
drink[1] = wine_list[0]+wine_list[1]
drink[2] = max(wine_list[0]+wine_list[2], wine_list[0]+wine_list[1], wine_list[1]+wine_list[2])

for i in range(3, n):
    drink[i] = max(drink[i-2]+wine_list[i], drink[i-3]+wine_list[i-1]+wine_list[i], drink[i-1])

print(drink)
print(drink[n-1])