def is_palindrome(x):
    return str(x) == str(x)[::-1]

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
num = n

while True:
    if is_palindrome(num) and is_prime(num):
        print(num)
        break
    num += 1
