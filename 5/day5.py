import re
input: str = './input'

# part 1
with open(input, 'r') as f:
    conf, moves = [x for x in f.read().split('\n\n')]

conf = conf.split('\n')
conf = conf[:len(conf)-1]
groups = [[line[x:x+4].strip(' []') for x in range(0, len(line), 4)]
          for line in conf[::-1]]


stacks = [[] for _ in range(len(groups[0]))]


for group in groups:
    for i, el in enumerate(group):
        if el:
            stacks[i].append(el)


moves = [re.findall(r'[0-9]+', x) for x in moves.split('\n')]

for move in moves:
    if not len(move):
        continue
    n, a, b = map(int, move)
    moved_crates = []
    for _ in range(n):
        moved_crates.append(stacks[a-1].pop())

    for crate in moved_crates[::-1]:
        stacks[b-1].append(crate)

print(''.join([s.pop() for s in stacks if len(s) > 0]))
