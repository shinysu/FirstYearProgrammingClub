from bs4 import BeautifulSoup
import requests


def get_content_from_url(url):
    """
    gets the html content from the webpage
    :param url: url of the webpage
    :return: HTML content of the page
    """
    try:
        url = url if url.startswith('http') else ('http://' + url)
        return requests.get(url).content
    except requests.ConnectionError as e:
        print("Connection Error: Could not connect to the server or not found.\n")
        print(str(e))
    except requests.Timeout as e:
        print("Timeout Error")
        print(str(e))
    except requests.RequestException as e:
        print("General Error")
        print(str(e))
    except KeyboardInterrupt:
        print("Keyboard interrupt")


def parse_html_by_tags(html, tag):
    """
    parses the HTML page and gets the text of the given tag
    :param html: the html content that is to be parsed
    :param tag: the tag for which the text data is to be returned
    :return: text data of the corresponding tag from the webpage
    """
    data = []
    if html:
        soup = BeautifulSoup(html, "html.parser")
        for para in soup.find_all(tag):
            data.append(para.text)
    return data
