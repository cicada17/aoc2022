# part 1
res = 0
with open('input/d4', 'r') as f:
    for rawline in f:
        line = rawline.rstrip()
        if len(line) == 0:
            continue
        range1, range2 = line.split(',')
        start1, end1 = [int(s) for s in range1.split('-')]
        start2, end2 = [int(s) for s in range2.split('-')]
        if start2 <= start1 and end1 <= end2:
            res += 1
        elif start1 <= start2 and end2 <= end1:
            res += 1

print(res)

# part 2
res = 0
with open('input/d4', 'r') as f:
    for rawline in f:
        line = rawline.rstrip()
        if len(line) == 0:
            continue
        range1, range2 = line.split(',')
        start1, end1 = [int(s) for s in range1.split('-')]
        start2, end2 = [int(s) for s in range2.split('-')]
        if start1 <= start2 <= end1:
            res += 1
        elif start2 <= start1 <= end2:
            res += 1

print(res)
