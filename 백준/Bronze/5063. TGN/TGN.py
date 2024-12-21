cnt = int(input())

for _ in range(cnt):
    
    r, e, c = map(int,input().split())
    gap =  e - c
    if gap > r:
        print("advertise")
    elif gap < r:
        print("do not advertise")
    else:
        print("does not matter")
