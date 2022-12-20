# part 1
res = 0
with open('input/d8', 'r') as f:
    fraw = f.read().rstrip('\n')
trees = [[int(s) for s in line] for line in fraw.split('\n') if line]
ni = len(trees)
nj = len(trees[0])
visible = [[0 for _ in range(nj)] for __ in range(ni)]

def mark_visible(i, j):
    global visible, current_max
    if trees[i][j] > current_max:
        visible[i][j] = 1
    current_max = max(current_max, trees[i][j])

for i in range(ni):
    current_max = -1
    for j in range(nj):
        mark_visible(i,j)
    
    current_max = -1
    for j in reversed(range(nj)):
        mark_visible(i,j)

for j in range(nj):
    current_max = -1
    for i in range(ni):
        mark_visible(i,j)
    
    current_max = -1
    for i in reversed(range(ni)):
        mark_visible(i,j)

res = sum(sum(row) for row in visible)

print(res)

# part 2
res = 0
with open('input/d8', 'r') as f:
    fraw = f.read().rstrip('\n')
for line in fraw.split('\n'):
    if len(line) == 0:
        continue

print(res)
