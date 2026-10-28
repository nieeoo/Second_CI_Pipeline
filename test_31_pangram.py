import importlib

module = importlib.import_module("31_pangram")

def test_pangram_true():
    assert module.is_pangram(
        "The quick brown fox jumps over the lazy dog"
    ) is True

def test_pangram_false():
    assert module.is_pangram("Hello World") is False

def test_pangram_uppercase():
    assert module.is_pangram(
        "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    ) is True