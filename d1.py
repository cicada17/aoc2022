# part 1
res = 0
s = 0
with open('input/d1', 'r') as f:
    for line in f:
        l = line.rstrip()
        if len(l) == 0:
            res = max(res, s)
            s = 0
            continue
        num = int(l)
        s += num

print(res)

# part 2
res = []
with open('input/d1', 'r') as f:
    for line in f:
        l = line.rstrip()
        if len(l) == 0:
            res.append(s)
            s = 0
            continue
        num = int(l)
        s += num

top3 = sorted(res)[-3:len(res)]
print(top3)
print(sum(top3))

