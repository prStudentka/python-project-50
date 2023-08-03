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
        return _DICT_CONVERT.get(elem['value'], f"'{elem['value']}'")
    return '[complex value]'


def formating(diffs, path=""):
    lines = []
    for item in diffs:
        head = f"{path}{item['name']}"
        level = f"Property '{head}' was "
        if item['meta'] == 'added':
            value = f"{level + item['meta']} with value: {convert(item)}"
            lines.append(value)
        if item['meta'] == 'removed':
            lines.append(level + item['meta'])
        if is_nest(item):
            if item['meta'] == 'updated':
                value = list(map(convert, item['children']))
                lines.append(f"{level + item['meta']}. From {(value[0])} to {value[1]}")
            elif item['meta'] == 'unchanged':
                value = formating(item['children'], f"{head}.")
                lines.append(f"{value}")
    return '\n'.join(lines)
