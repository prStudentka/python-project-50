import pytest
from gendiff.generate_diff import generate_diff as gdiff

_FILE1 = 'fixtures/file1.json'
_FILE2 = 'fixtures/file2.json'
_EXPECTED = '''
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

def test_parse_json():
    assert gdiff(_FILE1, _FILE2) == _EXPECTED
