input: str = './input'

# part 1
with open(input, 'r') as f:
    data = [[y.split('-') for y in x.split(',')] for x in f.read().strip().split('\n')]

count = 0

for a, b in data:
    a1, a2 = a
    b1, b2 = b
    if int(a1) <= int(b1) <= int(b2) <= int(a2) or int(b1) <= int(a1) <= int(a2) <= int(b2):
        count += 1

print(count)

# part 2
with open(input, 'r') as f:
    data = [[y.split('-') for y in x.split(',')] for x in f.read().strip().split('\n')]

count = 0

for a, b in data:
    a1, a2 = a
    b1, b2 = b
    if int(a1) <= int(b1) <= int(a2) or int(a1) <= int(b2) <= int(a2) or int(b1) <= int(a1) <= int(b2) or int(b1) <= int(a2) <= int(b2):
        count += 1

print(count)
