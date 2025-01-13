"""
1. 스택에 자기를 넣음
2. 스택이 비어있지 않고 자신과 스택의 tos의 문자가 같으면 tos 제거
3. 문자 추가
4. 반복 후 스택 비어있으면 1, 아니면 0 출력
"""
def solution(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return 1 if not stack else 0