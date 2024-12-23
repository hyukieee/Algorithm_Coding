str1 = input()
str2 = input()

arr1 = [0] * 26
arr2 = [0] * 26

for i in str1:
    idx = ord(i) - ord('a')
    arr1[idx] += 1
for i in str2:
    idx = ord(i) - ord('a')
    arr2[idx] += 1

result = [0] * 26

for i in range(26):
    result[i] += abs(arr1[i] - arr2[i])

print(sum(result))