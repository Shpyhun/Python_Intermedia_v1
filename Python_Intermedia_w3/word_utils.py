def sentence_without_punctuation(sentence):
    """Returns a sentence without punctuation"""
    new_sign = ''
    for sign in sentence:
        if sign not in r"!#$%&\'\"()*+,-./:;<=>?@[\\]^_`{|}~":
            new_sign += sign
    return new_sign


def word_list(sentence):
    """Returns a list of words from a sentence"""
    return sentence_without_punctuation(sentence).split()


def longest_word(sentence):
    """Returns the longest word in a sentence"""
    return max(word_list(sentence), key=len)
