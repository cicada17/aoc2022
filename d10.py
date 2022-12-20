# part 1
res = 0

def should_add(cycle):
    return (cycle - 20) % 40 == 0

cycle = 0
x = 1
with open('input/d10', 'r') as f:
    fraw = f.read().rstrip('\n')
for line in fraw.split('\n'):
    if len(line) == 0:
        continue
    
    if line == 'noop':
        cycle += 1
        res += should_add(cycle) * x * cycle
    else:
        # addx
        cycle += 2
        res += should_add(cycle) * x * cycle
        res += should_add(cycle - 1) * x * (cycle - 1)
        x += int(line.split()[1])

print(res)

# part 2
res = 0
with open('input/d10', 'r') as f:
    fraw = f.read().rstrip('\n')
for line in fraw.split('\n'):
    if len(line) == 0:
        continue

print(res)
