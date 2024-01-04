_DICT_CHANGE = {
    'removed': '- ',
    'added': '+ ',
    'unchanged': '  '
}
_DICT_CONVERT = {
    'False': 'false',
    'True': 'true',
    'None': 'null'
}
_INDENT = 4
_REPLACER = ' '


def is_nest(node):
    return node['type'] == 'nest'


def is_value(node):
    return node['type'] == 'value'


def convert(elem):
    return _DICT_CONVERT.get(str(elem), elem)


def format(diffs, lvl=1):
    result = ['{']
    indent = (_INDENT - 2) * _REPLACER

    def walk(values):
        for item in values:
            sign = _DICT_CHANGE.get(item['meta'], '')
            deep = f'{indent * lvl}{sign}{item["name"]}: '
            if is_value(item):
                value = f'{deep}{convert(item["value"])}'
                result.append(value)
            if is_nest(item):
                if sign:
                    value = f'{deep}{format(item["children"], lvl + 2)}'
                    result.append(value)
                else:
                    walk(item['children'])
    walk(diffs)
    result.append(f'{indent*(lvl-1)}}}')
    return '\n'.join(result)
