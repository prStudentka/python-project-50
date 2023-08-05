#!user/bin/env python3
from gendiff import generate_diff
from gendiff.generate_diff import get_args


def main():
    arg = get_args()
    diff = generate_diff(arg.first_file, arg.second_file, arg.format)
    print(diff)


if __name__ == '__main__':
    main()
