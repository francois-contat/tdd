import reverse_words

def test_reverse():
    result = reverse_words.reverse_words('')
    assert result == ''

def test_reverse_coucou():
    result = reverse_words.reverse_words('coucou')
    assert result == 'coucou'

def test_reverse_coucou_non():
    result = reverse_words.reverse_words('coucou non')
    assert result == 'non coucou'

def test_reverse_coucou_oui_non():
    result = reverse_words.reverse_words('coucou oui non')
    assert result == 'non oui coucou'

def test_reverse_bon_on_y_va_ou_pas():
    result = reverse_words.reverse_words('bon on y va ou pas')
    assert result == ('pas ou va y on bon')
