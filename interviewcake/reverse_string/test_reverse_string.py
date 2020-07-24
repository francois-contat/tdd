import reverse_string

def test_reverse_ah():
    result = reverse_string.reverse_str('ah')
    assert result == 'ha'

def test_reverse_a():
    result = reverse_string.reverse_str('a')
    assert result == 'a'

def test_reverse_aba():
    result = reverse_string.reverse_str('aba')
    assert result == 'aba'

def test_reverse_baab():
    result = reverse_string.reverse_str('baab')
    assert result == 'baab'

def test_reverse_abaab():
    result = reverse_string.reverse_str('abaab')
    assert result == 'baaba'

def test_reverse_institution():
    result = reverse_string.reverse_str('institution')
    assert result == 'noitutitsni'

def test_reverse_coucou():
    result = reverse_string.reverse_str('coucou')
    assert result == 'uocuoc'
