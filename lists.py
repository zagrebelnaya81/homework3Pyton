"""
high level support for doing this and that.
"""
LONG_TEXT = """asdlknfasldkmfasdfasdf"""

words = []


def add_word(word: str = ''):
    """Adds a new word to list of words"""
    if isinstance(word, str):
        words.append(word)
        return words
    return "word is not object of str class"


def get_words(chars: str):
    """Accepts chars and finds all the words which start with the chars.
    Returns a list of those words in ascending order (length must be up to 5)"""
    final = []
    if isinstance(chars, str):
        for word in words:
            index = word.find(chars)
            if index >= 0:
                final.append(word)
        final.sort()
        return final[:5]
    return "word is not object of str class"


def crop_text(length):
    """Generator yields a text piece of specified length or less"""
    while True:
        yield LONG_TEXT[:length]
        yield LONG_TEXT[length:length*2]
        yield LONG_TEXT[length*2:]


if __name__ == '__main__':
    assert get_words('') == []
    add_word('bat')
    add_word('batman')

    assert get_words('') == ['bat', 'batman']
    assert get_words('bat') == ['bat', 'batman']
    assert get_words('batm') == ['batman']
    assert get_words('x') == []
    add_word('bar')
    add_word('bartender')
    add_word('basket')
    add_word('band')
    assert get_words('ba') == ['band', 'bar', 'bartender', 'basket', 'bat']

    text_generator = crop_text(10)
    assert next(text_generator) == "asdlknfasl"
    assert next(text_generator) == "dkmfasdfas"
    assert next(text_generator) == "df"
