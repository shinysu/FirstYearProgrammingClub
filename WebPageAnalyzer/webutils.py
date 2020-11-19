from bs4 import BeautifulSoup
import requests
from utils import get_lines, get_words, get_top_words


def get_statistics(url):
    """
    Gets the webpage content from the url and determines the count of lines, words, unique words and the top 5 most
    frequent words from the page
    :param url: url of the web page
    :return: the count of lines, words, unique words and the top 5 most frequent words from the page
    """
    html_page = get_content_from_url(url)
    data = get_content_by_tags(html_page, 'p')
    lines = get_lines(data)
    words, unique_words = get_words(lines)
    top_words = get_top_words(words)
    return len(lines), len(words), len(unique_words), top_words


def get_content_from_url(url):
    """
    gets the html content from the webpage
    :param url: url of the webpage
    :return: HTML content of the page
    """
    try:
        return requests.get(url).content
    except requests.ConnectionError as e:
        print("Connection Error. Make sure you are connected to Internet.\n")
        print(str(e))
    except requests.Timeout as e:
        print("Timeout Error")
        print(str(e))


def get_content_by_tags(html, tag):
    """
    parses the HTML page and gets the text of the given tag
    :param html: the html content that is to be parsed
    :param tag: the tag for which the text data is to be returned
    :return: text data of the corresponding tag from the webpage
    """
    data = []
    soup = BeautifulSoup(html, "html.parser")
    for para in soup.find_all(tag):
        data.append(para.text)
    return data


if __name__ == "__main__":
    url = 'https://www.edutopia.org/article/help-students-build-intrinsic-motivation'
    line_count, words_count, unique_words, top_words = get_statistics(url)
    print(line_count)
    print(words_count)
    print(unique_words)
    print(top_words)

