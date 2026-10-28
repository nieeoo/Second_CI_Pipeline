import importlib

module = importlib.import_module("33_first_non_repeating")

def test_normal_string():
    assert module.first_non_repeating("swiss") == "w"

def test_first_character_unique():
    assert module.first_non_repeating("apple") == "a"

def test_no_non_repeating_character():
    assert module.first_non_repeating("aabb") is None

def test_empty_string():
    assert module.first_non_repeating("") is None