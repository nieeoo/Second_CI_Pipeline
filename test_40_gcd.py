import importlib

module = importlib.import_module("40_gcd")

def test_normal_numbers():
    assert module.gcd(12, 18) == 6

def test_coprime_numbers():
    assert module.gcd(7, 9) == 1

def test_negative_number():
    assert module.gcd(-12, 8) == 4

def test_zero():
    assert module.gcd(0, 5) == 5