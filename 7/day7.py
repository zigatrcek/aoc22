input: str = './input'

# part 1
with open(input, 'r') as f:
    data = f.read().strip().split('\n')

class File:
    def __init__(self, size):
        self.size = size

def get_current_dir(filesys, path):
    current_dir = filesys
    for dir in path:
        current_dir = current_dir[dir]
    return current_dir

def compute_size(dir):
    all_sizes = []
    size = 0
    for k, v in dir.items():
        if isinstance(v, dict):
            s, a = compute_size(v)
            size += s
            for x in a:
                all_sizes.append(x)
        else:
            size += v.size
    all_sizes.append(size)
    return size, all_sizes


current_path = []
filesys = {'/': {}}
for line in data:
    if line.startswith('$'):
        line = line.split(' ')
        if line[1] == 'ls':
            continue
        else:
            if line[2] == '..':
                current_path.pop()
            else:
                current_path.append(line[2])
    else:
        current = get_current_dir(filesys, current_path)
        line = line.split(' ')
        if line[0] == 'dir':
            current[line[1]] = {}
        else:
            current[line[1]] = File(int(line[0]))




size, all_sizes = compute_size(filesys['/'])
print(sum([x for x in all_sizes if x <= 100000]))

# part 2
total_size = 70000000
left_space = total_size - size
needed_space = 30000000 - left_space

all_sizes = sorted(all_sizes)
for a in all_sizes:
    if a >= needed_space:
        print(a)
        break
