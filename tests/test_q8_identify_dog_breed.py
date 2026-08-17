from q8_identify_dog_breed import identify_dog_breed


def test_identify_dog_breed():
    
    assert(identify_dog_breed(25, "short") == "Pembroke Welsh Corgi")
    assert(identify_dog_breed(95, "long") == "Old English Sheepdog")
    assert(identify_dog_breed(19, "medium") == "Mudi")
    assert(identify_dog_breed(50, "long") == "Collie")
    
