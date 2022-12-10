def calory(raw_text):
    return sum(int(line) for line in raw_text.split('\n'))

# part 1
res = 0
with open('input/d1', 'r') as f:
    raw_texts = [x for x in f.read().split('\n\n') if x]
    calories = [calory(raw_text) for raw_text in raw_texts]
    res = max(calories)

print(res)

# part 2
res = []
with open('input/d1', 'r') as f:
    raw_texts = f.read().rstrip('\n').split('\n\n')
    calories = [calory(raw_text) for raw_text in raw_texts]
    res = sorted(calories)[-3:]

print(res)
print(sum(res))

