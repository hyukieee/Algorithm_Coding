n = int(input())

for _ in range(n):
    num = int(input())
    result = 0
    for i in range(num//3 + 1):
        tmp = num - (3* i)
        result += (tmp//2) +1 
    
    print(result)