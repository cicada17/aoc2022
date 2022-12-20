class Monkey(object):
    def __init__(self):
        self.items = []
        self.op = ''
        self.op_value = 0
        self.divisor = 1
        self.next_true = 0
        self.next_false = 0

# part 1
monkeys = []
count = 0
res = 0
with open('input/d11', 'r') as f:
    fraw = f.read().rstrip('\n')
for monkey_raw in fraw.split('\n\n'):
    if not monkey_raw:
        continue
    monkey = Monkey()
    monkeys.append(monkey)
    for line in monkey_raw.split('\n'):
        if 'Starting' in line:
            items = [int(s) for s in line.split('Starting items: ')[1].split(', ')]
            monkey.items.extend(items)
        elif 'Operation' in line:
            if '+' in line:
                monkey.op = '+'
                monkey.op_value = int(line.split()[-1])
            elif '* old' in line:
                monkey.op = '^2'
            else:
                monkey.op = '*'
                monkey.op_value = int(line.split()[-1])
        elif 'divisible' in line:
            monkey.divisor = int(line.split()[-1])
        elif 'If true' in line:
            monkey.next_true = int(line.split()[-1])
        elif 'If false' in line:
            monkey.next_false = int(line.split()[-1])

inspect = [0 for _ in range(len(monkeys))]
for monkey in monkeys:
    print(monkey.items)
print()
for _ in range(20):
    for i, monkey in enumerate(monkeys):
        inspect[i] += len(monkey.items)
        for item in monkey.items:
            # Inspect
            if monkey.op == '+':
                item += monkey.op_value
            elif monkey.op == '*':
                item *= monkey.op_value
            else:
                item = item * item
            
            # Decrease worryness
            item = item // 3

            # Test
            if item % monkey.divisor == 0:
                monkeys[monkey.next_true].items.append(item)
            else:
                monkeys[monkey.next_false].items.append(item)
        monkey.items.clear()
    for monkey in monkeys:
        print(monkey.items)
    print()

inspect.sort()
res = inspect[-1] * inspect[-2]
print(res)

# part 2
res = 0
with open('input/d11', 'r') as f:
    fraw = f.read().rstrip('\n')
for line in fraw.split('\n'):
    if len(line) == 0:
        continue

print(res)
