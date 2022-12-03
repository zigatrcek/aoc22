input: str = './input'


def convert_to_int_value(c: str) -> int:
    i = ord(c)
    if i > 96:
        i = i - 96
    else:
        i = i - 65 + 27
    return i


# part 1
with open(input, 'r') as f:
    data = [[y for y in map(lambda z: convert_to_int_value(z), x)]
            for x in f.read().strip().split('\n')]

score = 0

for line in data:
    first, second = line[len(line)//2:], line[:len(line)//2]

    for x in first:
        if x in second:
            score += x
            break

print(score)


# part 2
with open(input, 'r') as f:
    data = [[y for y in map(lambda z: convert_to_int_value(z), x)]
            for x in f.read().strip().split('\n')]


groups = [data[x:x+3] for x in range(0, len(data), 3)]
score = 0

for group in groups:
    a, b, c = group
    for x in a:
        if x in b and x in c:
            score += x
            break
print(score)
