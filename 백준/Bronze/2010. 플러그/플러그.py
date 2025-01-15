import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
total_plugs = sum(int(data[i]) for i in range(1, N + 1))
result = total_plugs - N + 1
print(result)
