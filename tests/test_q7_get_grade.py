from q7_get_grade import get_grade

def test_get_grade():
    
    assert(get_grade(82, 93, 87, 64, 91) == 88.25) # prints "Average grade pre-curve: 88.25"
    assert(get_grade(75, 80, 85, 90, 95, curve=2) == 89.5) # prints "Average grade pre-curve: 87.5"
    assert(get_grade(75, 75, 75, 75, 75, curve=10) == 85) # prints "Average grade pre-curve: 75.0"
    
