N, K = map(int, input().split())
is_deleted = [False] * (N + 1)
deleted_count = 0

for P in range(2, N + 1):
    if not is_deleted[P]:
        for multiple in range(P, N + 1, P):
            if not is_deleted[multiple]:
                is_deleted[multiple] = True
                deleted_count += 1
                if deleted_count == K:
                    print(multiple)
                    exit()
