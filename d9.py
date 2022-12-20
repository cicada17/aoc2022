from collections import defaultdict

di_map = defaultdict(int)
dj_map = defaultdict(int)
di_map['U'] = -1
di_map['D'] = 1
dj_map['L'] = -1
dj_map['R'] = 1

# part 1
res = 0
with open('input/d9', 'r') as f:
    fraw = f.read().rstrip('\n')

max_length = sum(int(line.split()[1]) for line in fraw.split('\n') if line)
hi = max_length
hj = max_length
ti = max_length
tj = max_length
visited = [ [0 for _ in range(max_length*2)] for __ in range(max_length*2)]
visited[ti][tj] = 1
for line in fraw.split('\n'):
    if len(line) == 0:
        continue
    direction, stepnum = line.split()
    di = di_map[direction]
    dj = dj_map[direction]
    for _ in range(int(stepnum)):
        hi += di
        hj += dj
        if hi == ti and abs(hj - tj) > 1:
            tj += dj
        elif hj == tj and abs(hi - ti) > 1:
            ti += di
        elif hi != ti and hj != tj and abs(hi - ti) + abs(hj - tj) > 2:
            ti += 1 if hi > ti else -1
            tj += 1 if hj > tj else -1
        visited[ti][tj] = 1

res = sum(sum(row) for row in visited)
print(res)

# part 2
res = 0
with open('input/d9', 'r') as f:
    fraw = f.read().rstrip('\n')
for line in fraw.split('\n'):
    if len(line) == 0:
        continue

print(res)
