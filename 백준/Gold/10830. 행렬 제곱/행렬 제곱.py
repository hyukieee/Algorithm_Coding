def mult(A, B):
    N = len(A)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % 1000
    return result

def pow(A,B):
    N = len(A)
    result = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    
    while B > 0:
        if B % 2 == 1:
            result = mult(result, A)
            
        A = mult(A, A)
        B //= 2
    
    return result


N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


result = pow(A,B)

for row in result:
    print(' '.join(map(str, row)))