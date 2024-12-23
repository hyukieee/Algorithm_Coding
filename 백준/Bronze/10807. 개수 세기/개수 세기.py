n = int(input())
numbers = list(map(int,input().split()))
target  = int(input())

cnt = 0
for i in numbers:
    if(i == target):
        cnt += 1

print(cnt )