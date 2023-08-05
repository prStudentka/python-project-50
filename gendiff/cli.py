import argparse
import pathlib as path
import gendiff.parser_end as pe


def get_args():
    parser = argparse.ArgumentParser(
       description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output, default="stylish"')
    return parser.parse_args()


def start_cli():
    arg = get_args()
    path1, path2, _format = arg.first_file, arg.second_file, arg.format
    if path.Path(path1).exists() and path.Path(path2).exists():
        data1 = get_data(path1)
        data2 = get_data(path2)
        return data1, data2, _format
    else:
        raise FileNotFoundError('one of files not found')


def get_data(file):
    with open(file, 'r') as f:
        loader = pe.parser_suffix((path.PurePath(file).suffix)[1:])
        if loader is None:
            raise Exception('extention error')
        return loader(f)
