def parse(stack_lines):
    stacks = []
    stack_lines.reverse()
    transposed = [''.join(t) for t in zip(*stack_lines)]
    for stack_line in transposed:
        stack = [c for c in stack_line if c.isalpha()]
        if stack:
            stacks.append(stack)
    return stacks

# part 1
res = ''
read_stack = True
stack_lines = []
stacks = []
with open('input/d5', 'r') as f:
    raw = f.read().rstrip()
    stack_input, movement_input = raw.split('\n\n')
    stacks = parse(list(stack_input.split('\n')))
    for line in movement_input.split('\n'):
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
    raw = f.read().rstrip()
    stack_input, movement_input = raw.split('\n\n')
    stacks = parse(list(stack_input.split('\n')))
    for line in movement_input.split('\n'):
        num_and_space = ''.join(c for c in line if c.isdigit() or c == ' ')
        num_to_move, source, dest = [int(s) for s in num_and_space.split()]
        source -= 1
        dest -= 1
        temp = [stacks[source].pop() for i in range(num_to_move)]
        temp.reverse()
        stacks[dest] += temp

for stack in stacks:
    if len(stack) == 0:
        continue
    res += stack[-1]

print(res)
