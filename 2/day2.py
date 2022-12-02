input: str = './input'

# part 1
with open(input, 'r') as f:
    data = [[y for y in map(ord, x.split())] for x in f.read().strip().split('\n')]

score = 0
for pair in data:
    a, b = pair[0] - 65, pair[1] - 88

    score += b + 1
    if a == b:
        score += 3
    elif (a + 1) % 3 == b:
        score += 6

print(score)

# part 2
with open(input, 'r') as f:
    data = [[y for y in map(ord, x.split())] for x in f.read().strip().split('\n')]


score = 0
for pair in data:
    a, outcome = pair[0] - 65, pair[1] - 88
    if outcome == 0:
        b = (a - 1) % 3
    elif outcome == 1:
        b = a
        score += 3
    else:
        b = (a + 1) % 3
        score += 6
    score += b + 1


print(score)
