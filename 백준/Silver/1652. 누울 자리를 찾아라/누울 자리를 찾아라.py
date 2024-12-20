n = int(input())
arr = []

for i in range(n):
    row = input().strip() 
    arr.append(list(row)) 


Count1 = 0
# 세로 누울 자리
for r in range(n):
    cnt = 0
    for c in range(n):
        if(arr[r][c] == '.'):
            cnt += 1
        if(arr[r][c] == 'X'):   
            if(cnt >=2):
                Count1 += 1
            cnt =0
    if cnt >= 2:
        Count1 += 1

# 가로 누울 자리
Count2 = 0
for c in range(n):
    cnt = 0
    for r in range(n):
        if(arr[r][c] == '.'):
            cnt += 1
        if(arr[r][c] == 'X'):   
            if(cnt >=2):
                Count2 += 1
            cnt =0
    if cnt >= 2:
        Count2 += 1

print(Count1, Count2 )
