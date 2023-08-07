import pytest
import yaml
from gendiff.generate_diff import generate_diff as gdiff, get_data
from gendiff.parser_end import parser_suffix
import pathlib


_PATH = 'tests/fixtures/'
_FILE1 = pathlib.Path(_PATH, 'file1.json')
_FILE2 = pathlib.Path(_PATH, 'file2.json')
_TREE1 = pathlib.Path(_PATH, 'tree1.json')
_TREE2 = pathlib.Path(_PATH, 'tree2.json')
_FILE1_YML = pathlib.Path(_PATH, 'file1.yml')
_FILE2_YML = pathlib.Path(_PATH, 'file2.yaml')
_EXPECTED = pathlib.Path(_PATH, 'expected_json.txt')
_EXPECTED_TREE = pathlib.Path(_PATH, 'expected_tree.txt')
_EXPECTED_PLAIN = pathlib.Path(_PATH, 'expected_plain.txt')
_OUTPUT_JSON = pathlib.Path(_PATH, 'output_json.txt')


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


def test_exception_suffix():
    with pytest.raises(Exception) as error:
        get_data(_EXPECTED)
    assert str(error.value) == 'extention error'


def test_exception_file():
    with pytest.raises(FileNotFoundError) as error:
        gdiff('tests/file1.json', _FILE2)
    assert str(error.value) == 'one of files not found'


def test_wrong_format():
    result = gdiff(_FILE1, _FILE2, 'SAME')
    assert result == 'Wrong format'


@pytest.mark.parametrize(
    'input1, input2, expected',
    [
        pytest.param(
            _FILE1, _FILE2, _EXPECTED,
            id='files_json'),
        pytest.param(
            _FILE1_YML, _FILE2_YML, _EXPECTED,
            id='files_yaml')
    ])
def test_parse_generate_diff(input1, input2, expected):
    with open(expected, 'r') as f:
        report = f.read().rstrip()
    assert gdiff(input1, input2) == report


@pytest.mark.parametrize(
    'input1, input2, formats, expected',
    [
        pytest.param(
            _TREE1, _TREE2, 'stylish',
            open(_EXPECTED_TREE, 'r').read().rstrip(),
            id='test_stylish'),
        pytest.param(
            _TREE1, _TREE2, 'plain',
            open(_EXPECTED_PLAIN, 'r').read().rstrip(),
            id='test_plain'),
        pytest.param(
            _TREE1, _TREE2, 'json',
            open(_OUTPUT_JSON, 'r').read().rstrip(),
            id='test_output_json')
    ])
def test_format(input1, input2, formats, expected):
    assert gdiff(input1, input2, formats) == expected
