input: str = './input'

# part 1
with open(input, 'r') as f:
    data = f.read().strip()

chars = []
for c in data:
    chars.append(c)
    if len(chars) >= 4 and len(chars[-4:]) == len(set(chars[-4:])):
        print(len(chars))
        break


# part 2
with open(input, 'r') as f:
    data = f.read().strip()

chars = []
for c in data:
    chars.append(c)
    if len(chars) >= 14 and len(chars[-14:]) == len(set(chars[-14:])):
        print(len(chars))
        break
