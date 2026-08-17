from q1_average_and_show_work import average_and_show_work 

def test_average_and_show_work():
    assert(average_and_show_work(2, 2, 2) == None) # (2 + 2 + 2) / 3 = 6 / 3 = 2.0
    assert(average_and_show_work(5, 7, 11) == None) # (5 + 7 + 11) / 3 = 23 / 3 = 7.67
    assert(average_and_show_work(30, -17, 0) == None) # (30 + -17 + 0) / 3 = 13 / 3 = 4.33
    

