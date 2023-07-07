import pytest
from gendiff.generate_diff import generate_diff as gdiff

_FILE1 = 'tests/fixtures/file1.json'
_FILE2 = 'tests/fixtures/file2.json'
_EXPECTED = 'tests/fixtures/expected_json.txt'

def test_parse_json():
    result = gdiff(_FILE1, _FILE2)
    with open(_EXPECTED) as f:
      report = f.read()
    assert result == report
