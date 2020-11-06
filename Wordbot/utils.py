from nltk.corpus import wordnet as wn


def get_meaning(word):
    """
    get the meaning of the given word from wordnet
    :param word: string, the word for which meaning is to be found
    :return: string, the meaning of the word if the word is found in corpus; None otherwise
    """
    synset = wn.synsets(word)
    if synset:
        return synset[0].definition()
    else:
        return None


def get_synonyms(word):
    """
    get the synonyms for the given word from wordnet
    :param word: string, the word for which synonyms are to be found
    :return: the synonyms for the word
    """
    synonyms = []
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)


def get_antonyms(word):
    """
    get the antonyms for the given word from wordnet
    :param word: string, the word for which antonyms are to be found
    :return: the antonyms for the word
    """
    antonyms = []
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    return set(antonyms)


def convert_to_string(words_set):
    """
    converts a given set() to string
    :param words_set: the set of words
    :return: converted_string
    """
    converted_string = ', '.join(word for word in words_set)
    return converted_string
