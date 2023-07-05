#!user/bin/env python3
from gendiff import generate_diff
from gendiff.cli import start_diff


def main():
    start_diff(generate_diff)


if __name__ == '__main__':
    main()
