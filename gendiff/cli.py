import argparse


def start_diff(module):
    parser = argparse.ArgumentParser(
       description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    arg = parser.parse_args()
    file_path1, file_path2 = arg.first_file, arg.second_file
    diff = module.generate_diff(file_path1, file_path2)
    print(diff)
