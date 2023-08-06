import pytest
import yaml
import json
from gendiff.generate_diff import generate_diff as gdiff, get_data
from gendiff.parser_end import parser_suffix
import pathlib


_FILE1 = 'tests/fixtures/file1.json'
_FILE2 = 'tests/fixtures/file2.json'
_TREE1 = 'tests/fixtures/tree1.json'
_TREE2 = 'tests/fixtures/tree2.json'
_FILE1_YML = 'tests/fixtures/file1.yml'
_FILE2_YML = 'tests/fixtures/file2.yaml'
_EXPECTED = 'tests/fixtures/expected_json.txt'
_EXPECTED_TREE = 'tests/fixtures/expected_tree.txt'


def test_data():
    result_yml = get_data(_FILE1_YML)
    with open(_FILE1_YML, 'r') as f_yml:
        data_yml = yaml.safe_load(f_yml)
    assert data_yml == result_yml


def test_parser_suffix():
    assert pathlib.PurePath(_FILE2_YML).suffix == '.yaml'
    loader = parser_suffix('yaml')
    with open(_FILE2_YML, 'r') as f:
        result = loader(f)
    with open(_FILE2_YML, 'r') as df:
        data = yaml.safe_load(df)
    assert result == data
    loader = parser_suffix('json')
    with open(_FILE2, 'r') as jf:
        result = loader(jf)
    assert result == data


def test_parse_json():
    result = gdiff(_FILE1, _FILE2)
    with open(_EXPECTED, 'r') as f:
      report = f.read().rstrip()
    assert result == report
