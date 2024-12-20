def is_prime(n):
    if(n < 2 ) :
        return False
    for i in range(2,n):
        if(n%i  == 0 ) :
            return False
    return True

a = int(input())
cnt = 0

num = list(map(int,input().split() ))

for x in num:
    if(is_prime(x)== True):
        cnt += 1

print(cnt)