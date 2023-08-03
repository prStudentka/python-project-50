from gendiff.difference import differ as get_difference
from gendiff.formater.stylish import formating


def generate_diff(file1, file2, format='stylish'):
    dict_diff = get_difference(file1, file2)
    return formating(dict_diff)
