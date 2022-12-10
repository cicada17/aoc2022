class Folder(object):
    def __init__(self):
        self.parent = None
        self.children = {}
        self.size = 0

# part 1
res = 0
with open('input/d7', 'r') as f:
    fraw = f.read().rstrip('\n')
root = Folder()
current = root
raws = [r for r in fraw.split('$ ') if r]
for raw in raws:
    lines = [l for l in raw.split('\n') if l]
    # cd or empty ls
    if len(lines) == 1:
        line = lines[0]
        if line == 'cd ..':
            current = current.parent
        elif line == 'cd /':
            current = root
        elif 'cd' in line:
            name = line.split()[-1]
            if name in current.children:
                child = current.children[name]
            else:
                child = Folder()
                current.children[name] = child
                child.parent = current
            current = child
    # ls
    else:
        for line in lines:
            if line[0].isnumeric():
                current.size += int(line.split()[0])

sizes = []
def update_size(folder):
    size = folder.size + sum(update_size(child) for child in folder.children.values())

    sizes.append(size)
    folder.size = size

    return size

update_size(root)
res = sum(size for size in sizes if size < 100000)
print(res)

# part 2
current_empty = 70000000 - root.size
size_needed = 30000000 - current_empty
res = min(size for size in sizes if size > size_needed)
print(res)
