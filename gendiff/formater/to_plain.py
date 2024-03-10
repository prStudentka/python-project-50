_DICT_CONVERT = {
    '0': 0,
    'False': 'false',
    'True': 'true',
    'None': 'null'
}


def convert(elem):
    if not isinstance(elem['value'], list):
        return _DICT_CONVERT.get(f"{elem['value']}", f"'{elem['value']}'")
    return '[complex value]'


def get_plain(diffs, path=""):
    lines = []
    for item in diffs:
        head = f"{path}{item['name']}"
        level = f"Property '{head}' was "
        if item['status'] in ['removed', 'added', 'updated']:
            tail = ''
            if item['status'] == 'added':
                tail = f" with value: {convert(item)}"
            if item['status'] == 'updated':
                value = list(map(convert, item['value']))
                tail = f". From {value[0]} to {value[1]}"
            lines.append(f"{level}{item['status']}{tail}")
        if item['status'] == 'nested':
            value = get_plain(item['value'], f"{head}.")
            lines.append(f"{value}")
    return '\n'.join(lines)


def format(diff):
    return get_plain(diff)
