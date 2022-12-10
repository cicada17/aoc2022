# part 1
with open('input/d6', 'r') as f:
    for rawline in f:
        line = rawline.rstrip('\n')
        if len(line) == 0:
            continue
        # one line problem
        for i in range(len(line) - 4):
            window = line[i:i+4]
            if len(set(window)) == 4:
                print(i+4)
                break

# part 2
with open('input/d6', 'r') as f:
    for rawline in f:
        line = rawline.rstrip('\n')
        if len(line) == 0:
            continue
        # one line problem
        for i in range(len(line) - 14):
            window = line[i:i+14]
            if len(set(window)) == 14:
                print(i+14)
                break
