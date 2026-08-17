from q5_estimate_shipping_time import estimate_shipping_time

def test_estimate_shipping_time():
    
    assert(estimate_shipping_time("July", 12) == 10)
    assert(estimate_shipping_time("April", 4) == 7)
    assert(estimate_shipping_time("October", 7) == 7)
    assert(estimate_shipping_time("January", 8) == 10)
    assert(estimate_shipping_time("December", 2) == 15)
    assert(estimate_shipping_time("December", 24) == 15)
    assert(estimate_shipping_time("December", 25) == 20)
    
