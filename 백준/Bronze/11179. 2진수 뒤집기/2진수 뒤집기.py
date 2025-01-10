n = int(input())
result = []

while n != 0:
    result.append(n%2)
    n //= 2

answer = 0
N=1
for _ in range(len(result)):
    
    answer += result.pop()*N
    N *= 2
print(answer)