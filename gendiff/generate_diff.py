from gendiff.difference import differ as get_difference
from .formater.stylish import formating as stylish
from .formater.plain import formating as plain
from .formater.to_json import formating as js
import argparse
import pathlib as path
import gendiff.parser_end as pe


_DICT_FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': js
}


def get_args():
    text = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output, default="stylish"')
    return parser.parse_args()


def get_data(file):
    with open(file, 'r') as fi:
        loader = pe.parser_suffix((path.PurePath(file).suffix)[1:])
        if loader is None:
            raise Exception('extention error')
        return loader(fi)


def generate_diff(path1, path2, format='stylish'):
    if path.Path(path1).exists() and path.Path(path2).exists():
        file1 = get_data(path1)
        file2 = get_data(path2)
        dict_diff = get_difference(file1, file2)
        return _DICT_FORMATS.get(format, 'Wrong format')(dict_diff)
    else:
        raise FileNotFoundError('one of files not found')
