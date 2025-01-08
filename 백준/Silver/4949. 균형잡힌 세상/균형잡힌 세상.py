while True:
    arr = input()
    if arr == '.':
        break
    
    stack = []
    ret = True

    for char in arr:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                ret = False
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                ret = False
                break

    if ret and not stack:
        print("yes")
    else:
        print("no")
