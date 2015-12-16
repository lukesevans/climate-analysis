# Test script for temperature conversion 

from temp_conversion import fahr_to_kelvin
from nose.tools import *

def test_zero_kelvin():
    assert round(fahr_to_kelvin(-459.67),2)==0

@raises(TypeError)
def test_null_entry():
    assert fahr_to_kelvin()

@raises(TypeError)
def test_temp_string():
    assert fahr_to_kelvin("SomeTemperature")
