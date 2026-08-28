""" Question 1: average_and_show_work """
"""
Inputs: three integers
Output: print out the calculation of the average of these three integers
        returns nothing
"""
def average_and_show_work(x, y, z):
    mid_result = (x + y + z)
    final_result = round(mid_result / 3, 2)
    first_str = "(" + str(x) + " + " + str(y) + " + " + str(z) + ") / 3"
    second_str = str(mid_result) + " / 3"
    final_str = str(final_result)
    print(first_str + " = " + second_str + " = " + final_str)
    return 


""" Test 1 """
def test_average_and_show_work():
    print("Testing average_and_show_work...")
    # Check whether each call prints the expected text
    assert(average_and_show_work(2, 2, 2) == None) # (2 + 2 + 2) / 3 = 6 / 3 = 2.0
    assert(average_and_show_work(5, 7, 11) == None) # (5 + 7 + 11) / 3 = 23 / 3 = 7.67
    assert(average_and_show_work(30, -17, 0) == None) # (30 + -17 + 0) / 3 = 13 / 3 = 4.33
    print("... done!")


if __name__ == '__main__':
    test_average_and_show_work()
