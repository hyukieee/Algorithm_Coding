def solution(N, stages):
    people = [0] * (N+2)
    
    
    for i in stages: 
        people[i] += 1
    
    
    fail = {}
    
    total = len(stages)
    
    for i in range(1,N+1):
        if people[i] == 0 :
            fail[i] = 0
        else:
            fail[i] = people[i] / total
            total -= people[i]
    
    ret = sorted(fail, key = lambda x : fail[x], reverse = True)
        
        
    return ret