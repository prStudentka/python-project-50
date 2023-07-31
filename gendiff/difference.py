def mkvalue(key, value, meta='unchanged'):
    return {
        'name': key,
        'value': value,
        'meta': meta,
        'type': 'value'
    }


def mknest(key, children, meta='unchanged'):
    return {
        'name': key,
        'children': children,
        'meta': meta,
        'type': 'nest'
    }


def choose_fill(key, item, meta='unchanged'):
    if type(item) is not dict:
        return mkvalue(key, item, meta)
    children = []
    for key_item in item.keys():
        children.append(choose_fill(key_item, item[key_item]))
    return mknest(key, children, meta)


def differ(data1, data2):
    def walk(key):
        if key not in data1:
            return choose_fill(key, data2[key], 'add')
        elif key not in data2:
            return choose_fill(key, data1[key], 'remove')
        elif data1[key] == data2[key]:
            return mkvalue(key, data1[key])
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            return mknest(key, differ(data1[key], data2[key]))
        else:
            change_dict = choose_fill(key, data1[key], 'remove')
            change_dict2 = choose_fill(key, data2[key], 'add')
            return mknest(key, [change_dict, change_dict2], 'change')
    return list(map(walk, sorted((data1.keys() | data2.keys()))))
