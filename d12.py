from collections import deque

# part 1

def reachable(current, target):
    if current == 'S':
        return True
    if target == 'E':
        return current == 'z' or current == 'y'
    return ord(target) - ord(current) <= 1

res = 0
with open('input/d12', 'r') as f:
    fraw = f.read().rstrip('\n')
hill = [line for line in fraw.split('\n') if line]
ni = len(hill)
nj = len(hill[0])

si, sj = 0, 0
for i in range(ni):
    for j in range(nj):
        if hill[i][j] == 'S':
            si, sj = i, j

visited = [[0 for _ in range(nj)] for __ in range(ni)]

def run_bfs():
    bfs = deque([(si, sj, 0)])
    while bfs:
        ci, cj, distance = bfs.popleft()
        if visited[ci][cj]:
            continue
        visited[ci][cj] = distance + 1
        if hill[ci][cj] == 'E':
            return distance
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ti = ci + di
            tj = cj + dj
            if not 0 <= ti < ni:
                continue
            if not 0 <= tj < nj:
                continue
            if reachable(hill[ci][cj], hill[ti][tj]):
                bfs.append((ti, tj, distance + 1))

res = run_bfs()
for line in visited:
    print(line)
print(res)

# part 2
res = 0
with open('input/d12', 'r') as f:
    fraw = f.read().rstrip('\n')
for line in fraw.split('\n'):
    if len(line) == 0:
        continue

print(res)
