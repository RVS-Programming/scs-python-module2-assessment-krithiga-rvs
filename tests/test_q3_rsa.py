from q3_rsa import encode
from q3_rsa import decode
from q3_rsa import transmit


def test_rsa():
    
    assert(encode(402, 7, 697) == 326)
    assert(encode(213, 7, 697) == 2)
    assert(encode(1234, 143, 50573) == 42522)

    assert(decode(326, 23, 697) == 402)
    assert(decode(2, 23, 697) == 213)
    assert(decode(42522, 16427, 50573) == 1234)

    assert(transmit(402, 7, 23, 697) == 402) # prints "Transmitting: 326"
    assert(transmit(213, 7, 23, 697) == 213) # prints "Transmitting: 2"
    assert(transmit(1234, 143, 16427, 50573) == 1234) # prints "Transmitting: 42522"
    
