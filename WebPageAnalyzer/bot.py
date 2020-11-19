"""
bot.py : Given an url, analyses the webpage and gives the following information about the page
            1. Number of sentences in the webpage
            2. Number of words in the page
            3. Number of unique words in the page
            4. 5 most frequent words in the page
"""

import PySimpleGUI as sg
from webutils import get_statistics

layout = [
            [sg.Text("Enter URL", font=("Arial", 14)), sg.InputText("", key="url", font=("Arial", 14)),
             sg.Button("Get Data", font=("Arial", 14), key='get')],
            [sg.Multiline(key="output", font=("Arial", 14), size=(60, 15), disabled=True)],
        ]

def get_and_display_statistics(url):
    """
    Analyses the web page of the url and displays the count of lines, word, unique words and the 5 most frequent words
    :param url: the url of the web page that is to be analysed
    """
    line_count, words_count, unique_words, top_words = get_statistics(url)
    display_statistics(line_count, words_count, unique_words, top_words)


def display_statistics(line_count, words_count, unique_words, top_words):
    """
    displays the count of lines, word, unique words and the 5 most frequent words
    :param line_count: the number of sentences in the web page
    :param words_count: the number of words in the web page
    :param unique_words: the number of unique words in the page
    :param top_words: 5 most frequent words in the page
    """
    window['output'].print("The web page consists of the following information:\n")
    window['output'].print(line_count, "sentences")
    window['output'].print(words_count, "words")
    window['output'].print(unique_words, "unique words")
    window['output'].print("\nThe top words are\n")
    for word, count in top_words:
        window['output'].print(word)


if __name__ == '__main__':
    window = sg.Window('WebPageAnalyzer', layout)
    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'get':
            get_and_display_statistics(values['url'])
    window.Close()

