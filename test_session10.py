import pytest

from session10 import *

fake_profiles_namedtuple, fake_profiles_dict = create_fake_profiles(seed = 0)


def test_namedtuple():
    results = calculate_namedtuple(fake_profiles_namedtuple)
    #assert add(1,2) == 3, "func add not working in odd seconds"

def test_dict():
    results = calculate_dict(fake_profiles_dict)
    #assert add(1,2) == 3, "func add not working in odd seconds"
