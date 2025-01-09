def solution(s):
    idx = 0
    answer = 0
    equal = 0
    nonEqual= 0
    
    for i in range(len(s)):
        first = s[idx] 
        if s[i] == first:
            equal +=1
        else :
            nonEqual +=1
        
        if equal == nonEqual:
            answer += 1
            equal = 0
            nonEqual = 0
            idx = i+1
        
    if equal != nonEqual:
        answer += 1
        
    return answer