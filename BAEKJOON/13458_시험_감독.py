N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = N

for i in range(N):
    if A[i] > B:
        result += (A[i] - B) // C
        if (A[i] - B) % C:
            result += 1

print(result)