n = int(input())

numbers = list(map(int, input().split()))

target = int(input())

arr = [0] * 1000001

for i in numbers: 
    arr[i] += 1

count = 0

for i in numbers:
    idx = target - i
    if 1 <= idx <= 1000000:
        count += arr[idx]
        if idx == i:
            count -= 1

print(count // 2)
