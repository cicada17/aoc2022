import functools

def priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

# part 1
res = 0
with open('input/d3', 'r') as f:
    for rawline in f:
        line = rawline.rstrip()
        if len(line) == 0:
            continue
        s1 = set(line[:len(line)//2])
        s2 = set(line[len(line)//2:])
        for c in s1:
            if c in s2:
                res += priority(c)

print(res)

# part 2
res = 0
count = 0
badges = set()
with open('input/d3', 'r') as f:
    lines = f.read().rstrip('\n').split('\n')
    for i in range(len(lines) // 3):
        group = [set(line) for line in lines[3*i:3*i+3]]
        commons = functools.reduce(set.intersection, group)
        for c in commons:
            res += priority(c)

print(res)
