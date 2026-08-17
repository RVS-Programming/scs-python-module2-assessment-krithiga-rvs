""" Question 8: identify_dog_breed """
"""
Inputs: weight (integer) and coat_length (string)
Output: corresponding dog breed (see Workbook for table)
"""
def identify_dog_breed(weight, coat_length):
    if weight < 20:
        if coat_length == "short":
            return "Swedish Vallhund"
        elif coat_length == "medium":
            return "Mudi"
        else:
            return "Shetland Sheepdog"
    elif weight < 50:
        if coat_length == "short":
            return "Pembroke Welsh Corgi"
        elif coat_length == "medium":
            return "Australian Shepherd"
        else:
            return "Bearded Collie"
    elif weight < 80:
        if coat_length == "short":
            return "Belgian Malinois"
        elif coat_length == "medium":
            return "German Shepherd"
        else:
            return "Collie"
    else:
        if coat_length == "short":
            return "Beauceron"
        elif coat_length == "medium":
            return "Bouvier des Flandres"
        else:
            return "Old English Sheepdog"

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