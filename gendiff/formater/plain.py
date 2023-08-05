_DICT_CONVERT = {
    False: 'false',
    True: 'true',
    None: 'null'
}


def is_nest(node):
    return node['type'] == 'nest'


def is_value(node):
    return node['type'] == 'value'


def convert(elem):
    if is_value(elem):
        return _DICT_CONVERT.get(f'{elem['value']}', f"'{elem['value']}'")
    return '[complex value]'


def formating(diffs, path=""):
    lines = []
    for item in diffs:
        head = f"{path}{item['name']}"
        level = f"Property '{head}' was "
        if item['meta'] in ['removed', 'added',  'updated']:
            tail = ''
            if item['meta'] == 'added':
                tail = f" with value: {convert(item)}"
            if item['meta'] == 'updated':
                value = list(map(convert, item['children']))
                tail = f". From {(value[0])} to {value[1]}"
            lines.append(f"{level}{item['meta']}{tail}")
        if is_nest(item) and item['meta'] == 'unchanged':
            value = formating(item['children'], f"{head}.")
            lines.append(f"{value}")
    return '\n'.join(lines)
