import sys
input = sys.stdin.readline
print = sys.stdout.write
from queue import Queue


def lca(first, second):
    if depth[first] < depth[second]:
        first, second = second, first

    log = 1
    while True:
        if (1 << log) > depth[first]: break
        else: log += 1
    log -= 1

    for i in range(log, -1, -1):
        if depth[first] - (1 << i) >= depth[second]:
            first = p[first][i]

    if first == second:
        return first
    else:
        for i in range(log, -1, -1):
            if p[first][i] != 0 and p[first][i] != p[second][i]:
                first = p[first][i]
                second = p[second][i]
        return parent[first]


n = int(input())
v = [[] for _ in range(n+1)]
q = Queue()
check = [False] * (n+1)
parent = [0] * (n+1)
depth = [0] * (n+1)
p = [[0 for _ in range(18)] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

check[1] = True
parent[1] = 0
depth[1] = 0
q.put(1)
while not q.empty():
    node = q.get()
    for next in v[node]:
        if not check[next]:
            check[next] = True
            parent[next] = node
            depth[next] = depth[node] + 1
            q.put(next)

for i in range(1, n+1):
    p[i][0] = parent[i]

for j in range(n):
    if (1 << j) < n:
        for i in range(1, n+1):
            if p[i][j-1] != 0:
                p[i][j] = p[p[i][j-1]][j-1]
    else:
        break

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print("%d\n" % lca(a, b))
