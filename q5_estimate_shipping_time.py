""" Question 5: estimate_shipping_time """
"""
Inputs: a month (string) and day (integer)
Output: shipping time needed to ship an item on specified date with special cases:
        1. Most items ship in 10 days
        2. December is busy so items that ship in December take 5 days longer
        3. December 25 - end of year is even busier, so items shipped then take 
           5 more days
        4. Items that ship before the 7th of the month take 3 fewer days
           (This rule doesn't apply to December)
"""
def estimate_shipping_time(month, day):
    est = 10
    if month == "December":
        est = est + 5
        if day >= 25:
            est = est + 5
    elif day <= 7:
        est = est - 3
    return est

""" Test 5 """
def test_estimate_shipping_time():
    print("Testing estimate_shipping_time...", end="")
    assert(estimate_shipping_time("July", 12) == 10)
    assert(estimate_shipping_time("April", 4) == 7)
    assert(estimate_shipping_time("October", 7) == 7)
    assert(estimate_shipping_time("January", 8) == 10)
    assert(estimate_shipping_time("December", 2) == 15)
    assert(estimate_shipping_time("December", 24) == 15)
    assert(estimate_shipping_time("December", 25) == 20)
    print("... done!")

if __name__ == '__main__':
    test_estimate_shipping_time()