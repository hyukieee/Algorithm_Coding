def dfs(start, visited, connected):
    visited[start] = True
    for i in connected[start]:
        if not visited[i]:
            dfs(i, visited, connected)

n = int(input()) # computer 
m = int(input()) # connected pair

network = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

dfs(1, visited, network)

print(sum(visited) -1)