import importlib

module = importlib.import_module("38_missing_number_xor")

def test_middle_missing():
    assert module.missing_number([3, 0, 1]) == 2

def test_last_missing():
    assert module.missing_number([0, 1, 2, 3]) == 4

def test_only_zero():
    assert module.missing_number([]) == 0