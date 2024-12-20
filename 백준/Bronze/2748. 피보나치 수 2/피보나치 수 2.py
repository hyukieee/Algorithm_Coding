def fibo(n):
    a = 0
    b = 1 
    for i in range(n):
        a,b = a+b, a
        
    """ 
    for i in range(n):
        tmp = a
        a += b
        b = tmp
    """
    return a
    

n = int(input())

print(fibo(n))