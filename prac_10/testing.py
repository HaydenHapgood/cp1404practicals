"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return  len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi", "Hi test fail."
    print("Hi test passed.")
    # TODO: 1. fix the repeat_string function above so that it passes the failing test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"
    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car odometer test fail."
    print('Car test passed.')

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    car = Car(fuel=10)
    assert car.fuel == 10, "Car fuel test fail."
    print('Car fuel test passed.')

run_tests()

# TODO: 3. Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()

# TODO: 4. Fix the failing is_long_word function
# (Don't change the tests, change the function!)

# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
def phrase_as_sentence(phrase):
    phrase = phrase.replace(".", "").strip()
    return phrase.lower().capitalize() + "."

assert phrase_as_sentence('hello') ==  'Hello.', 'Phrase to sentence test 1 fail.'
print('Phrase to sentence test 1 passed.')
assert phrase_as_sentence('It is an ex parrot.') == 'It is an ex parrot.', 'Phrase to sentence test 2 fail.'
print('Phrase to sentence test 2 passed.')
assert phrase_as_sentence('H.E.L.L.O.') == 'Hello.', 'Phrase to sentence test 3 fail.'
print('Phrase to sentence test 3 passed.')
# and one more that you decide is a useful test.
# Run your doctests and watch the tests fail.
# Then write the body of the function so that the tests pass.
