"""
bot.py : Given a word, gets the meaning, synonyms and antonyms for the word
"""
import PySimpleGUI as sg
from utils import get_meaning, get_synonyms, get_antonyms, convert_to_string

greeting = "Hi, I am a word bot. I can help you with words\n"

layout = [
    [sg.Multiline(greeting, font=("Arial", 14), size=(70, 15), key='output')],
    [sg.InputText("", font=("Arial", 14), size=(50, 1), key='input', enable_events=True)],
    [sg.Button("Meaning", font=("Arial", 14), bind_return_key=True, key='meaning'),
     sg.Button("Synonyms", font=("Arial", 14), bind_return_key=True, key='synonym'),
     sg.Button("Antonyms", font=("Arial", 14), bind_return_key=True, key='antonym'),
     sg.Button("Clear", font=("Arial", 14), bind_return_key=True, key='clear')
    ]
]

def display_meaning(word):
    """
    Displays the word and the meaning of the word
    :param word: string, input word
    """
    meaning = get_meaning(word)
    window['output'].print("WORD: " + word)
    if meaning:
        window['output'].print("MEANING: ", meaning)
    else:
        display_error("Word is not found in corpus")


def display_synonyms(word):
    """
    Displays the word and the synonyms of the word. Throws an error if the word has no synonyms in corpus
    :param word: string, input word
    """
    window['output'].print("WORD: ", word)
    synonyms = get_synonyms(word)
    if synonyms:
        window['output'].print("SYNONYM: " + convert_to_string(synonyms))
    else:
        display_error("No synonyms found for the word in corpus")


def display_antonyms(word):
    """
    Displays the word and the antonyms of the word. Throws an error if the word has no antonyms in corpus
    :param word: string, input word
    """
    window['output'].print("WORD: ", word)
    antonym = get_antonyms(word)
    if antonym:
        window['output'].print("ANTONYM: " + convert_to_string(antonym))
    else:
        display_error("No antonyms found for the word in corpus")


def display_error(message):
    """
    Displays an error message in the output window
    :param message: string, the error message to be displayed
    """
    window['output'].print("ERROR: " + message, text_color='red')


def clear_window():
    """clears the output window"""
    window['output'].Update(greeting)
    window['input'].Update('')


if __name__ == '__main__':
    window = sg.Window('File Explorer', layout)

    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'meaning':
            display_meaning(values['input'])
        elif event == 'synonym':
            display_synonyms(values['input'])
        elif event == 'antonym':
            display_antonyms(values['input'])
        elif event == 'clear':
            clear_window()
    window.Close()
