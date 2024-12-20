def max(a,b):
    while b:
        tmp = b
        b = a % b
        a = tmp
    return a


a,b = (int(x) for x in input().split())

Max = max(a,b)

print(Max)
print((a*b)//Max)

