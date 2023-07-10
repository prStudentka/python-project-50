from json import load as jload
from yaml import safe_load as yload


def parser_suffix(suffix):
    if suffix == 'json':
        return jload
    elif suffix in ['yml', 'yaml']:
        return yload
