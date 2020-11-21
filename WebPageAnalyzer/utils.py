import re
import string
from collections import Counter
top_n = 5


def get_statistics(data):
    """
    Analyses the webpage data and returns the count of lines, words and unique words and the top 5 most frequent words
    from the page
    :param data: the data from the webpage that is to be analysed
    :return: the count of lines, words and unique words and the top 5 most frequent words from the page
    """
    lines = get_lines(data)
    words, unique_words = get_words(lines)
    top_words = get_top_words(words, top_n)
    statistics = {'line_count': len(lines), 'words_count': len(words), 'unique_words': len(unique_words),
                  'top_words': top_words}
    return statistics


def clean_string(inp_str):
    """
    Cleans the string; removes the punctuations in the string, converts the string to lower case and splits the string
    into words
    :param inp_str: the input line that is to be cleaned
    :return: a list of words in the input string
    """
    st = str.maketrans('“–”', '   ', string.punctuation)
    return inp_str.translate(st).lower().strip().split()


def get_lines(text):
    """
    splits the input string into sentences
    :param text: input string
    :return: a list of sentences in the input string
    """
    lines = []
    for parah in text:
        para_lines = re.split(r'[.!?]+', parah)
        lines.extend(para_lines)
    return lines


def get_words(lines):
    """
    Determines the number of words and the count of unique words in the input string
    :param lines: input string
    :return:
        1. list of words in the string
        2. list of unique words in the string
    """
    words = []
    for line in lines:
        line_words = clean_string(line)
        words.extend(line_words)
    unique_words = list(set(words))
    return words, unique_words


def get_top_words(words, top_n):
    """
    Gets the top n most frequent words from a given list of words
    :param words: list of words
    :param top_n: the count of most frequent words to be returned
    :return: the n most frequent words and their frequency of occurance
    """
    stopwords = get_stop_words()
    words_cleaned = [word for word in words if word not in stopwords]
    return Counter(words_cleaned).most_common(top_n)


def get_stop_words():
    """
    Reads the file 'stopwords.txt' and gets the list of stopwords
    :return: list of stopwords
    """
    with open('stopwords.txt', "r") as fp:
        words = fp.readlines()
        stopwords = [word.rstrip('\n') for word in words]
    return stopwords
