def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combination(balls, share):
    return factorial(balls) // (factorial(share) * factorial(balls - share))

def solution(balls, share):
    return combination(balls, share)
