import sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    a.append((int(input()), i))

swap_cnt = 0
sorted_a = sorted(a)

for i in range(n):
    if swap_cnt < sorted_a[i][1] - i:
        swap_cnt = sorted_a[i][1] - i
print(swap_cnt + 1)