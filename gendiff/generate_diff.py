from gendiff.difference import differ as get_difference
from .formater.stylish import formating as stylish
from .formater.plain import formating as plain
from .formater.to_json import formating as js
from gendiff.cli import start_cli


_DICT_FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': js
}


def start_diff():
    file1, file2, _format = start_cli()
    diff = generate_diff(file1, file2, _format)
    print(diff)


def generate_diff(file1, file2, format='stylish'):
    dict_diff = get_difference(file1, file2)
    return _DICT_FORMATS.get(format, 'Wrong format')(dict_diff)
