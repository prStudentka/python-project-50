import argparse
import pathlib as path
import parser_end as pe

def start_diff(module):
    parser = argparse.ArgumentParser(
       description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    arg = parser.parse_args()
    path1, path2 = arg.first_file, arg.second_file
    if path.Path(path1).exists() and path.Path(path2).exists():
        loader1 = get_loader(path1)
        loader2 = get_loader(path2)
        diff = module.generate_diff(loader1(f1), loader2(path2))
        print(diff)
    raise FileNotFoundError('one of files not found')


def get_loader(file):
    with open(file, 'r') as f:
        loader = pe.parser_suffix((path.PurePath(f).suffix)[1:])
        if loader is None:
            raise Exception('extention error')
        return loader
    
