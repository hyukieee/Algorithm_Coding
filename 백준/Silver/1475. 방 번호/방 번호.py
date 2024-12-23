numbers = input()

arr = [0]* 10

for num in numbers:
    if(int(num) == 6 or int(num) == 9):
        idx = 6
    else :
        idx = int(num)
    arr[idx] += 1

temp = arr[6]%2
arr[6] = arr[6]//2 + temp

result = max(arr)
print(result)