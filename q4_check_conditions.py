""" Question 4: check_conditions """
"""
Inputs: three integers 
Output: True if at least one of the following is true:
        1. Both x and y are greater than 10
        2. Either one of y or z is odd
"""
def check_conditions(x, y, z):
    return (x > 10 and y > 10) or (not (y % 2 == 0 or z % 2 == 0))

""" Test 4 """
def test_check_conditions():
    print("Testing check_conditions...", end="")
    assert(check_conditions(12, 14, 7) == True)
    assert(check_conditions(15, 1, 9) == True)
    assert(check_conditions(10, 12, -2) == False)
    assert(check_conditions(19, 16, 4) == True)
    assert(check_conditions(1, 3, 5) == True)
    print("... done!")

if __name__ == '__main__':
    test_check_conditions()