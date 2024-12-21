m ,n = map(int, input().split())

listen = []
for _ in range(m):
    string = input()
    listen.append(string)

see = []
for _ in range(n):
    string = input()
    see.append(string)

noHearSee = sorted(set(listen) & set(see))
print(len(noHearSee))
print('\n'.join(noHearSee))