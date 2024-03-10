def make_value(key, value, status='unchanged'):
    return {
        'name': key,
        'value': value,
        'status': status,
    }


def convert(elem):
    if not isinstance(elem, dict):
        return elem

    def walk(key):
        return make_value(key, convert(elem[key]))
    return list(map(walk, elem.keys()))


def differ(data1, data2):
    def walk(key):
        if key not in data1:
            return make_value(key, convert(data2[key]), 'added')
        elif key not in data2:
            return make_value(key, convert(data1[key]), 'removed')
        elif data1[key] == data2[key]:
            return make_value(key, convert(data1[key]))
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            return make_value(key, differ(data1[key], data2[key]), 'nested')
        else:
            change_dict = make_value(key, convert(data1[key]), 'removed')
            change_dict2 = make_value(key, convert(data2[key]), 'added')
            return make_value(key, [change_dict, change_dict2], 'updated')
    return list(map(walk, sorted((data1.keys() | data2.keys()))))
