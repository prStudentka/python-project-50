from gendiff.difference import differ as get_difference
from .formater.to_stylish import formating as stylish
from .formater.to_plain import formating as plain
from .formater.to_json import formating as js
import argparse
import pathlib as pathl
import gendiff.parser_end as parse


_DICT_FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': js
}


def get_args():
    text = 'Compares two configuration files and look at the difference.'
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output, default="stylish"')
    return parser.parse_args()


def get_data(path):
    with open(path, 'r') as file:
        loader = parse.parse_suffix((pathl.PurePath(path).suffix)[1:])
        if loader is None:
            raise Exception('extention error')
        return loader(file)


def generate_diff(path1, path2, format='stylish'):
    if pathl.Path(path1).exists() and pathl.Path(path2).exists():
        file1 = get_data(path1)
        file2 = get_data(path2)
        dict_diff = get_difference(file1, file2)
        if format in _DICT_FORMATS:
            return _DICT_FORMATS[format](dict_diff)
        return 'Wrong format'
    else:
        raise FileNotFoundError('one of files not found')
