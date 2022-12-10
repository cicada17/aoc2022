def parse(stack_lines):
    stacks = []
    stack_lines.reverse()
    transposed = [''.join(t) for t in zip(*stack_lines)]
    for stack_line in transposed:
        if not stack_line[0].isnumeric():
            continue
        stack = [c for c in stack_line if c.isalpha()]
        stacks.append(stack)
    return stacks

# part 1
res = ''
read_stack = True
stack_lines = []
stacks = []
with open('input/d5', 'r') as f:
    for rawline in f:
        line = rawline.rstrip('\n')
        # read stack
        if read_stack:
            if len(line) > 0:
                stack_lines.append(line)
            else:
                read_stack = False
                stacks = parse(stack_lines)
                print(stacks)
        # read movement
        else:
            if len(line) == 0:
                continue
            num_and_space = ''.join(c for c in line if c.isdigit() or c == ' ')
            num_to_move, source, dest = [int(s) for s in num_and_space.split()]
            source -= 1
            dest -= 1
            for i in range(num_to_move):
                stacks[dest].append(stacks[source].pop())

for stack in stacks:
    if len(stack) == 0:
        continue
    res += stack[-1]

print(res)

# part 2
res = ''
read_stack = True
stack_lines = []
stacks = []
with open('input/d5', 'r') as f:
    for rawline in f:
        line = rawline.rstrip('\n')
        # read stack
        if read_stack:
            if len(line) > 0:
                stack_lines.append(line)
            else:
                read_stack = False
                stacks = parse(stack_lines)
                print(stacks)
        # read movement
        else:
            if len(line) == 0:
                continue
            num_and_space = ''.join(c for c in line if c.isdigit() or c == ' ')
            num_to_move, source, dest = [int(s) for s in num_and_space.split()]
            source -= 1
            dest -= 1
            temp = []
            for i in range(num_to_move):
                temp.append(stacks[source].pop())
            temp.reverse()
            stacks[dest] += temp

for stack in stacks:
    if len(stack) == 0:
        continue
    res += stack[-1]

print(res)
