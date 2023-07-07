from json import load


def generate_diff(first_file, second_file):
    with (open(first_file, 'r') as f1,
          open(second_file, 'r') as f2):
        file1 = load(f1)
        file2 = load(f2)
        key = sorted(set(list(file1.keys()) + list(file2.keys())))
        data = ['{']
        for name in key:
            diff = f'    {name}: {file1.get(name)}'
            if name not in file2:
                diff = diff.replace('   ', '  -', 1)
            elif name not in file1:
                diff = f'  + {name}: {file2.get(name)}'
            elif file1[name] != file2[name]:
                diff = f'  - {name}: {file1[name]}\n  + {name}: {file2[name]}'
            data.append(diff.lower())
        data.append('}\n')
    return '\n'.join(data)
