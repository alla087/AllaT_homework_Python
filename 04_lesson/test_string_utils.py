import pytest
from string_utils import StringUtils

@pytest.mark.parametrize('input_text, expected_output',
    [
      ('Hello', 'Hello'),
      ('hello','Hello'),
      ('.','.'),
      ('',''),
      ('123','123'),
     ])
def test_string_capitalize(input_text, expected_output):
    test_capitalize = StringUtils()
    assert test_capitalize.capitalize(input_text) == expected_output
@pytest.mark.parametrize('input_text, expected_output',
    [
        (' Hello', 'Hello'),
        ('Hello', 'Hello'),
        ('   Hello', 'Hello'),
        ('Hello    ', 'Hello    '),
        ('Hello world', 'Hello world'),
        ('   Hello world', 'Hello world')
    ])
def test_string_trim(input_text, expected_output):
    test_trim = StringUtils()
    assert test_trim.trim(input_text)== expected_output

@pytest.mark.parametrize('input_text, symbol,result',
    [
        ('Hello', 'H',True),
        ('Hello', 'o', True),
        ('Hello', 'о', False), #проверяемый символ на кириллице
        ('Bye', 's',False),
        ('Country','1',False),
        ('City','й', False),
        ('Town', '!', False),
        ('House', ' ', False)
    ])
def test_string_contains(input_text, symbol, result):
    test_contains =StringUtils()
    assert test_contains.contains(input_text,symbol)== result

@pytest.mark.parametrize('input_text,deleted_symbol, result',
    [
        ('Hello', 'o', 'Hell'),
        ('Hello world', ' world', 'Hello'),
        ('Hello', '123','Hello'),
        ('Hello', ' ', 'Hello'),
        ('Hello','!', 'Hello'),
        ("Hello", 'о', 'Hello'),#  удаляемый символ на  кириллице

    ])
def test_string_delete(input_text, deleted_symbol, result):
    test_delete = StringUtils()
    assert test_delete.delete_symbol(input_text, deleted_symbol) == result