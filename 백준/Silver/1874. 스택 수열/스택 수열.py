# stack을 이용하여 수열을 만들 수 있는지 판별
def stack_numList(n, numList):
    stack = []
    result = []
    current = 1
    for number in numList:
        while current <= number:
            stack.append(current)
            result.append('+')
            current += 1
        if stack and stack[-1] == number:
            stack.pop()
            result.append('-')
        else:
            return -1 # 수열 생성 불가능 
    return result

# main 
n = int(input())
numList = [int(input()) for _ in range(n)]

output = stack_numList(n, numList)

if output == -1:
    print("NO")
else:
    print("\n".join(output))
