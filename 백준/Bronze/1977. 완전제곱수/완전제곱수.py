import math
M = int(input())
N = int(input())

pow = []

start = math.ceil(math.sqrt(M))
end = math.floor(math.sqrt(N))

for i in range(start, end + 1):
    square = i * i
    pow.append(square)

perfect_squares = [x for x in pow if M <= x <= N]
if pow:
    print(sum(pow))
    print(min(pow))
else:
    print(-1)