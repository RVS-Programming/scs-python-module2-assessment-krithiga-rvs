from q6_is_nice_outside import is_nice_outside

def test_is_nice_outside():
    
    assert(is_nice_outside(-10, False, False) == False)
    assert(is_nice_outside(72, True, True) == False)
    assert(is_nice_outside(0, False, True) == False)
    assert(is_nice_outside(69, True, False) == True)
    assert(is_nice_outside(102, True, False) == False)
    assert(is_nice_outside(5, False, False) == True)
    
