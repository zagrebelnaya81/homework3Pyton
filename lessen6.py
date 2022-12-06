"""Lesson 6"""
WORDS = {}
WORDS = {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}, 'TERM': 'hell'}}, 'TERM': 'he'}}}


def flatten(arr):
    """Generator that creates a flattened sequence from sequence of sequences"""
    for i in arr:
        for k in i:
            yield k


def grep(pattern):
    """Coroutine that accepts a search token and returns a string if it contains that token"""
    message = []
    while True:
        message = yield message if pattern in message else None


def add_word(word):
    """Method that adds a word into a dict of words in a specific way (see examples below)"""
    length = len(word)
    for i in range(length):
        recurse_add(WORDS, word[i], i, word)

    return WORDS


def recurse_add(dictionary: dict, letter: str, i: int, word: str):
    """Recursive function"""
    if len(dictionary.keys()) == 0:
        dictionary[letter] = {}
        return dictionary
    for _, item in dictionary.items():
        if isinstance(item, dict):
            return recurse_add(item, letter, i, word)
    return None


def get_words_recursive(words, chars, setwords):
    """Returns a list of words which start with passed characters.
       Length of the returned list must be up to 10 words"""
    for key in words.keys():
        if key == "TERM" and words[key].startswith(chars):
            setwords.add(words[key])
        if isinstance(words[key], dict):
            get_words_recursive(words[key], chars, setwords)
    return setwords


def get_words(chars):
    """Returns a list of words which start with passed characters.
          Length of the returned list must be up to 10 words"""
    setwords = set()
    get_words_recursive(WORDS, chars, setwords)
    if len(get_words_recursive(WORDS, chars, setwords)) == 0 or len(get_words_recursive(WORDS, chars, setwords)) >10:
        return list(setwords)
    return setwords


if __name__ == '__main__':
    assert not list(flatten([]))
    assert not list(flatten([[]]))
    assert not list(flatten([[], []]))
    assert list(flatten([[1, 2], [], [3]])) == [1, 2, 3]
    assert list(flatten([[1, 2], [3, 4, 5]])) == [1, 2, 3, 4, 5]
    #
    search = grep('bbq')
    next(search)

    assert search.send('Birthday invitation') is None
    assert search.send('Bring bbq sauce with') == 'Bring bbq sauce with'
    assert search.send('Are you hungry?') is None
    assert search.send("We won't invite you to our BBQ party then") is None
    assert search.send('but you better be quick (bbq) otherwise') == \
           'but you better be quick (bbq) otherwise'
    search.close()
    # print(add_word('hello'))
    # assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}}}}}}
    # print(add_word('hell'))
    # # assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}, 'TERM': 'hell'}}}}}
    # print(add_word('he'))
    # # assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}, 'TERM': 'hell'}},
    # #                              'TERM': 'he'}}}
    #
    assert set(get_words('he')) == {'he', 'hell', 'hello'}
    assert get_words('l') == []
    assert set(get_words('hel')) == {'hell', 'hello'}
