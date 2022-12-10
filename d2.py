# 1 for Rock, 2 for Paper, and 3 for Scissors
# 1 + 0,1,2
# 0 if you lost, 3 if the round was a draw, and 6 if you won
# 3 * (0,1,2)

# part 1
res = 0
with open('input/d2', 'r') as f:
    for rawline in f:
        line = rawline.rstrip()
        if len(line) == 0:
            continue
        op, me = line.split(' ')
        op = ord(op) - ord('A')
        me = ord(me) - ord('X')
        res += me + 1
        diff = (me - op) % 3
        if diff == 0:
            res += 3
        elif diff == 1:
            res += 6

print(res)

# part 2
res = 0
with open('input/d2', 'r') as f:
    for rawline in f:
        line = rawline.rstrip()
        if len(line) == 0:
            continue
        op, goal = line.split(' ')
        op = ord(op) - ord('A')
        goal = ord(goal) - ord('X')

        res += 1

        if goal == 0: # lose
            res += (op - 1) % 3
        if goal == 1: # draw
            res += op
        if goal == 2: # win
            res += (op + 1) % 3
        res += goal * 3

print(res)
