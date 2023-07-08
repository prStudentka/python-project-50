from json import load as jload
from pyyaml import safe_load as yload


def parser_suffix(suffix):
    if suffix == 'json':
        return jload
    elif suffix in ['yml', 'yaml']:
        return yload
