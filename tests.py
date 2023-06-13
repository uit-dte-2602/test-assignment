#imports
import pytest
import my_file

def test_my_function():
    answer = "python"
    result = my_file.my_function()
    assert result == answer