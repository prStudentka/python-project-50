_DICT_CHANGE = {
    'removed': '- ',
    'added': '+ ',
    'unchanged': '  ',
    'nested': '  '
}

_DICT_CONVERT = {
    'False': 'false',
    'True': 'true',
    'None': 'null'
}

_INDENT = 4
_REPLACER = ' '


def convert(elem):
    return _DICT_CONVERT.get(str(elem), elem)


def get_stylish(diffs, lvl=1):
    result = ['{']
    indent = (lvl * _INDENT - 2) * _REPLACER

    def walk(values):
        for item in values:
            sign = _DICT_CHANGE.get(item['status'], '')
            deep = f'{indent}{sign}{item["name"]}: '
            if item['status'] == 'nested':
                value = f'{deep}{get_stylish(item["value"], lvl + 1)}'
                result.append(value)
            elif item['status'] == 'updated':
                walk(item['value'])
            else:
                if isinstance(item["value"], list):
                    value = f'{deep}{get_stylish(item["value"], lvl + 1)}'
                    result.append(value)
                else:
                    value = f'{deep}{convert(item["value"])}'
                    result.append(value)

    walk(diffs)
    result.append(f'{(_INDENT * (lvl - 1)) * _REPLACER}}}')
    return '\n'.join(result)


def format(diff):
    return get_stylish(diff)
