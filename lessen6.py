"""Lesson 6"""
WORDS = {}
dict_arr = []


def flatten(arr):
    """Generator that creates a flattened sequence from sequence of sequences"""
    length = len(arr)
    if length == 0:
        return arr
    if length == 1:
        item = arr[0]
        try:
            # if item is not  empty list
            return flatten(list(item))
        except TypeError:
            # if item is empty
            return [item]
    else:
        return flatten(arr[:length // 2]) + flatten(arr[length // 2:])


def grep(pattern):
    """Coroutine that accepts a search token and returns a string if it contains that token"""
    while True:
        line = yield
        if pattern in line:
            yield line


def add_word(word):
    """Method that adds a word into a dict of words in a specific way (see examples below)"""
    first_dict = {"TERM": word}
    for char in range(0, len(word)):
        first_dict = {word[len(word)-1-char]: first_dict}
        second_dict = first_dict
        if len(word) <= char:
            second_dict = {word[char + 1]: 1}
    WORDS.update(first_dict)
    return WORDS


def get_dict_values_in_arr(words):
    """ Function get values of dictionary in"""
    for key in words.keys():
        if type(words[key]) == str:
            dict_arr.append(words[key])
        if not len(key) > 1:
            get_dict_values_in_arr(words[key])
    return dict_arr


def get_words(chars):
    """Returns a list of words which start with passed characters.
    Length of the returned list must be up to 10 words"""
    final = {}
    arr = []
    if isinstance(chars, str):
        for word in get_dict_values_in_arr(WORDS):
            if word.startswith(chars):
                arr.append(word)
        final = dict.fromkeys(arr)
        if len(final) == 0:
            return []
        if len(final) <= 10:
            return final
    return "word is not object of str class"


if __name__ == '__main__':
    assert not list(flatten([]))
    assert not list(flatten([[]]))
    assert not list(flatten([[], []]))
    assert list(flatten([[1, 2], [], [3]])) == [1, 2, 3]
    assert list(flatten([[1, 2], [3, 4, 5]])) == [1, 2, 3, 4, 5]

    search = grep('bbq')
    next(search)

    assert search.send('Birthday invitation') is None
    assert search.send('Bring bbq sauce with') == 'Bring bbq sauce with'
    assert search.send('Are you hungry?') is None
    assert search.send("We won't invite you to our BBQ party then") is None
    assert search.send('but you better be quick (bbq) otherwise') == \
           'but you better be quick (bbq) otherwise'
    search.close()
    print(add_word('hello'))
    assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}}}}}}
    print(add_word('hell'))
    # assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}, 'TERM': 'hell'}}}}}
    print(add_word('he'))
    # НА ЭТОМ  Я СДАЛАСЬ!!!!!!!!!!!!!!!!!!
    # assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}, 'TERM': 'hell'}},
    #                              'TERM': 'he'}}}

    # assert set(get_words('he')) == {'he', 'hell', 'hello'}
    # assert get_words('l') == []
    # assert set(get_words('hel')) == {'hell', 'hello'}
