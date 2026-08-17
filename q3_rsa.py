""" Question 3: RSA """
"""
Write three functions - encode, decode, and transmit - that transmits a message
with RSA encryption. 
"""
def encode(m, e, n):
    return

def decode(m, d, n):
    return

def transmit(message, e, d, n):
    return

""" Test 3 """
def test_rsa():
    print("Testing RSA functions...")
    # We'll test using two valid sets of RSA keys:
    # A: e = 7, d = 23, n = 697 [generated from p=17, q=41]
    # B: e = 143, d = 16427, n = 50573 [generated from p=491, q=103]
    assert(encode(402, 7, 697) == 326)
    assert(encode(213, 7, 697) == 2)
    assert(encode(1234, 143, 50573) == 42522)

    assert(decode(326, 23, 697) == 402)
    assert(decode(2, 23, 697) == 213)
    assert(decode(42522, 16427, 50573) == 1234)

    assert(transmit(402, 7, 23, 697) == 402) # prints "Transmitting: 326"
    assert(transmit(213, 7, 23, 697) == 213) # prints "Transmitting: 2"
    assert(transmit(1234, 143, 16427, 50573) == 1234) # prints "Transmitting: 42522"
    print("... done!")


if __name__ == '__main__':
    test_rsa()