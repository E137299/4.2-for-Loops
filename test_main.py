from main import *

def test_numbers_in_string():
    assert numbers_in_string(5) == "0 1 2 3 4 5 "
    assert numbers_in_string(3) == "0 1 2 3 "
    assert numbers_in_string(6) == "0 1 2 3 4 5 6 "

def test_factorial():
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(7) == 5040

def test_count_as():
    assert count_as("banana") == 3
    assert count_as("Go Austin High") == 1
    assert count_as("I ate some albacore tuna.") == 4

def test_multiples_of_3():
    assert multiples_of_3(10) == "3 6 9 "
    assert multiples_of_3(15) == "3 6 9 12 15 "
    assert multiples_of_3(13) == "3 6 9 12 15 "



def test_count_cat_words():
    assert count_cat_words(["catalog", "catapult", "dog", "scatter", "concatenate"]) == 4
    assert count_cat_words(["catchy", "dog", "vacate", "cattle"]) == 3