def isPrime(max_num):
    arr = [True] * (max_num + 1)
    arr[0] = arr[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if arr[i]:
            for j in range(i * i, max_num + 1, i):
                arr[j] = False
    return arr

def printPrimes(M, N):
    is_prime = isPrime(N)
    for number in range(M, N + 1):
        if is_prime[number]:
            print(number)

M, N = map(int, input().split())
printPrimes(M, N)
