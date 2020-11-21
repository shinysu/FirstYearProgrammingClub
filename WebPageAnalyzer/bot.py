"""
bot.py : Given an url, analyses the webpage and gives the following information about the page
            1. Number of sentences in the webpage
            2. Number of words in the page
            3. Number of unique words in the page
            4. 5 most frequent words in the page
"""

import PySimpleGUI as sg
from webutils import get_content_from_url, parse_html_by_tags
from utils import get_statistics


layout = [
            [sg.Text("Enter URL", font=("Arial", 14)), sg.InputText("", key="url", font=("Arial", 14)),
             sg.Button("Get Data", font=("Arial", 14), key='get', bind_return_key=True)],
            [sg.Multiline(key="output", font=("Arial", 14), size=(60, 15), disabled=True)],
        ]


def get_details(url):
    """
    Gets the webpage content for the url and determines the count of lines, words, unique words and the top 5 most
    frequent words from the page
    :param url: url of the web page
    """
    html_page = get_content_from_url(url)
    data = parse_html_by_tags(html_page, 'p')
    statistics = get_statistics(data)
    display_statistics(statistics)


def display_statistics(statistics):
    """
    Analyses the web page of the url and displays the count of lines, word, unique words and the 5 most frequent words
    :param statistics: the count of lines, words and unique words and the top 5 most frequent words from the page
    """
    window['output'].Update('')
    window['output'].print("The web page consists of the following information:\n")
    window['output'].print(statistics['line_count'], "sentences")
    window['output'].print(statistics['words_count'], "words")
    window['output'].print(statistics['unique_words'], "unique words")
    window['output'].print("\nThe top words are\n")
    for word, count in statistics['top_words']:
        window['output'].print(word)


if __name__ == '__main__':
    window = sg.Window('WebPageAnalyzer', layout)
    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'get':
            get_details(values['url'])
    window.Close()

