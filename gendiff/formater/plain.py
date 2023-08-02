_DICT_CONVERT = {
    False: 'false',
    True: 'true',
    None: 'null'
}

def is_nest(node):
    return node['type'] == 'nest'


def convert(elem):
    if is_value(elem):
        return _DICT_CONVERT.get(elem['value'], f"'{elem['value']}'")
    return '[complex value]'


def formating(diffs, path=""):
    lines = []
    for item in diffs:
        head = f"{path}{item['name']}"
        if item['meta'] != 'unchanged':
            level = f"Property '{head}' was {item['meta']}"
            if item['meta'] == 'added':
                value = f"{level} with value: {convert(item)}"
                lines.append(value)
            elif item['meta'] == 'removed':
                lines.append(level)
        if is_nest(item):
            if item['meta'] == 'updated':
                value =list(map(convert, item['children']))
                lines.append(f"{level}. From {(value[0])} to {value[1]}")
            elif item['meta'] == 'unchanged':
                value = formating(item['children'], f"{head}.")
                lines.append(f"{value}")
    return '\n'.join(lines)
