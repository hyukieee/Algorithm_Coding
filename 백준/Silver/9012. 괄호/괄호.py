n = int(input())
for _ in range(n):
    stack = input().strip()
    brace = []

    for i in stack:
        if i == '(':
            brace.append(i)
        elif i == ')':
            if brace:
                brace.pop()
            else:
                print("NO")
                break
    else:
        if not brace:
            print("YES")
        else:
            print("NO")