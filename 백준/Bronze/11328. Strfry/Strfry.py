n = int(input())

for _ in range(n):
    original , nonOri = map(str,input().split())
    ori_arr = [0] * 26
    non_arr = [0] * 26
    
    for i in original:
        idx = ord(i) - ord('a')
        ori_arr[idx] += 1
    for i in nonOri:
        idx = ord(i) - ord('a')
        non_arr[idx] += 1
    
    if(non_arr == ori_arr):
        print("Possible")
    else :
        print("Impossible")