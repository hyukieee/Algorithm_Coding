N, K = map(int,input().split())

boy = [0] * 7
girl = [0] * 7

for i in range(N):
    sex, grade = map(int,input().split())
    if(sex == 0 ):
        boy[grade] += 1
    elif(sex == 1 ):
        girl[grade] += 1

room = 0

for i in range(1,7):
    tmp1 = boy[i] % K
    tmp2 = girl[i] % K
    if(tmp1 > 0 ):
        room = room + boy[i]//K + 1
    else : 
        room = room + boy[i]//K

    if(tmp2 > 0 ):
        room = room + girl[i]//K + 1
    else : 
        room = room + girl[i]//K

print(room)