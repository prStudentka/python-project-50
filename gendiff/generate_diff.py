from json import load


def generate_diff(file1, file2):
    with (open(file1, 'r') as f1, open(file2, 'r') as f2):
        first_file = load(f1)
        second_file = load(f2)
        key = sorted(set(list(first_file.keys()) + list(second_file.keys())))
        data = ['{']
        for name in key:
            l = f'  {name}: {first_file.get(name)}'
            if name not in second_file:
                l = l.replace(' ', '-', 1)
            elif name not in first_file:
                l = f'+ {name}: {second_file.get(name)}'
            elif first_file[name] != second_file[name]:
                l = f'- {name}: {first_file.get(name)}\n\t+ {name}: {second_file.get(name)}'
            data.append('\t' + l)
        data.append('}')  
    return '\n'.join(data)
