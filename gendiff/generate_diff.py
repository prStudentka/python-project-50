from difference import differ as get_difference
from formater.stylish import formating

def differ(data1, data2):
    def walk(key):
        if key not in data1:
            return choose_fill(key, data2[key], 'add')
        elif key not in data2:
            return choose_fill(key, data1[key], 'remove')
        elif data1[key] == data2[key]:
            return mkvalue(key, data1[key])
        if isinstance(data1[key],dict) and isinstance(data2[key], dict):
            return mknest(key, differ(data1[key], data2[key]))
        else:
            change_dict = choose_fill(key, data1[key], 'remove')
            change_dict2 = choose_fill(key, data2[key], 'add')
            return mknest(key, [change_dict, change_dict2], 'change')
    return list(map(walk, sorted((data1.keys() | data2.keys()))))


def generate_diff(file1, file2, format='stylish'):
    # diff - разница словарь
    # stylish - отображение
    if str(file1).count('{') > 1:
        dict_diff = get_difference(file1, file2)
        return formating(dict_diff)
    key = sorted(set(list(file1.keys()) + list(file2.keys())))
    data = ['{']
    for name in key:
        differ = f'    {name}: {file1.get(name)}'
        if name not in file2:
            differ = differ.replace('   ', '  -', 1)
        elif name not in file1:
            differ = f'  + {name}: {file2.get(name)}'
        elif file1[name] != file2[name]:
            differ = f'  - {name}: {file1[name]}\n  + {name}: {file2[name]}'
        data.append(differ.lower())
    data.append('}\n')
    return '\n'.join(data)
