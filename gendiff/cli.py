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
        with (open(path1, 'r') as f1,
              open(path2, 'r') as f2):
            loader1 = pe.parser_suffix((path.PurePath(f1).suffix)[1:])
            loader2 = pe.parser_suffix((path.PurePath(f2).suffix)[1:])
            if loader1 is not None and loader2 is not None:
                diff = module.generate_diff(loader1(f1), loader2(path2))
                print(diff)
    raise FileNotFoundError('one of files not found')
    
