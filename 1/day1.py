input: str = './input'

# part 1
with open(input, 'r') as f:
    data = max([sum([int(num) for num in x.split('\n')]) for x in f.read().strip().split('\n\n')])
print(data)

# part 2
with open(input, 'r') as f:
    data = sum(sorted([sum([int(num) for num in x.split('\n')]) for x in f.read().strip().split('\n\n')], reverse=True)[:3])
print(data)
