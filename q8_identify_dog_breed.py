""" Question 8: identify_dog_breed """
"""
Inputs: weight (integer) and coat_length (string)
Output: corresponding dog breed (see Workbook for table)
"""
def identify_dog_breed(weight, coat_length):
    return

""" Test 8 """
def test_identify_dog_breed():
    print("Testing identify_dog_breed...", end="")
    assert(identify_dog_breed(25, "short") == "Pembroke Welsh Corgi")
    assert(identify_dog_breed(95, "long") == "Old English Sheepdog")
    assert(identify_dog_breed(19, "medium") == "Mudi")
    assert(identify_dog_breed(50, "long") == "Collie")
    print("... done!")

if __name__ == '__main__':
    test_identify_dog_breed()