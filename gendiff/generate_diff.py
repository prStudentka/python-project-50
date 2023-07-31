from gendiff.difference import differ as get_difference
from gendiff.formater.stylish import formating


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
