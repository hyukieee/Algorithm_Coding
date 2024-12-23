string = input()

arr = [0] * 26

for i in string:
    idx = ord(i) - ord('a')
    arr[idx] +=1

print(' '.join(map(str,arr)))