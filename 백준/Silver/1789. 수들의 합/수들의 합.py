import math

S = int(input())

N = int((-1 + math.sqrt(1 + 8 * S)) // 2)
while N * (N + 1) // 2 > S:
    N -= 1

print(N)
