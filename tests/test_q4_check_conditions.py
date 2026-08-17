from q4_check_conditions import check_conditions 

def test_check_conditions():
    
    assert(check_conditions(12, 14, 7) == True)
    assert(check_conditions(15, 1, 9) == True)
    assert(check_conditions(10, 12, -2) == False)
    assert(check_conditions(19, 16, 4) == True)
    assert(check_conditions(1, 3, 5) == True)
    
