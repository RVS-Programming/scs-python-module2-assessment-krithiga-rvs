""" Question 6: Debug the Function """
def fahrenheit_to_celsius(temp):
    return (temp - 32) * (5 / 9)

def is_nice_outside(temperature, in_fahrenheit, is_raining):
    if in_fahrenheit:
        temperature = fahrenheit_to_celsius(temperature)
    return (not is_raining) and ((temperature > 4) and (temperature < 35))

""" Test 6 """
def test_is_nice_outside():
    print("Testing is_nice_outside...", end="")
    assert(is_nice_outside(-10, False, False) == False)
    assert(is_nice_outside(72, True, True) == False)
    assert(is_nice_outside(0, False, True) == False)
    assert(is_nice_outside(69, True, False) == True)
    assert(is_nice_outside(102, True, False) == False)
    assert(is_nice_outside(5, False, False) == True)
    print("... done!")

if __name__ == '__main__':
    test_is_nice_outside()