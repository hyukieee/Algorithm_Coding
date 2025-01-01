def whatKg(kg):
    for x in range(kg//5,-1,-1):
        tmp = kg - (5*x)
        if tmp % 3 ==0 :
            y = tmp // 3
            return x+y
    return -1



kg = int(input())

result = whatKg(kg)
print(result)

