def find(n, lst):
    young = old = lst[0]
    
    for student in lst:
        name, day, month, year = student
        birth = (int(year), int(month), int(day))
        
        if birth > (int(young[3]), int(young[2]), int(young[1])):
            young = student
        
        if birth < (int(old[3]), int(old[2]), int(old[1])):
            old = student
    
    return young[0], old[0]

n = int(input())
lst = [input().split() for _ in range(n)]

young_name, old_name = find(n, lst)

print(young_name)
print(old_name)
