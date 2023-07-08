import pytest
from gendiff.generate_diff import generate_diff as gdiff
from gendiff.parser_end import parser_file

_FILE1 = 'tests/fixtures/file1.json'
_FILE2 = 'tests/fixtures/file2.json'
_FILE1_YML = 'tests/fixtures/file1.yml'
_FILE2_YML = 'tests/fixtures/file2.yaml'
_EXPECTED = 'tests/fixtures/expected_json.txt'


def test_parser_end():
    assert parser_file('tests/fixtures/expected_json.txt') == False

def test_parse_json():
    result = gdiff(_FILE1, _FILE2)
    with open(_EXPECTED, 'r') as f:
      report = f.read()
    assert result == report
