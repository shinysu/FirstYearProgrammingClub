import PySimpleGUI as sg
from utils import find_all_subdirectories, find_files
import datetime

layout = [
    [sg.Text('File Explorer - Find files/directories on your drive', font=("Arial", 20))],
    [sg.Text('Choose the path', font=("Arial", 14)), sg.InputText("", size=(40, 1), font=("Arial", 14), key='path',
                                                                  disabled=True, enable_events=True),
     sg.FolderBrowse(font=("Arial", 14))],
    [sg.Text('Enter a filter expression (for example: .jpg or .txt using wildcards)', font=("Arial", 14)),
    sg.InputText("", font=("Arial", 14), size=(10, 1), key='filter', enable_events=True)],
    [sg.Checkbox('Display Directories', font=("Arial", 14), key='directories'),
     sg.Button("Find...", font=("Arial", 14), bind_return_key=True, key='find'),
     sg.Button("Clear", font=("Arial", 14), bind_return_key=True, key='clear')],
    [sg.Output(font=("Arial", 14), size=(80, 15), key='output')]
]

def get_current_date():
    dt = datetime.datetime.now()
    date = dt.strftime("%Y-%m-%d %H:%M")
    return date


def display_files_directories(path, filter_expr):
    directories, files, stats = find_all_subdirectories(path, filter_expr)
    date = get_current_date()
    for directory in directories:
        print(date + "\t" + "<DIR>\t" + directory)
    for file, size in files.items():
        print(date + "\t" + "<FILE>\t" + file + "\t\t" + str(size) + " bytes")
    print()
    print(str(stats['total_files']) + " File(s)" + '\t' + str(stats['total_file_size']) + " bytes")
    print(str(stats['total_directories']) + " Dir(s)" + '\t' + str(stats['free_disk_space']) + " bytes free")


def display_files(path, filter_expr):
    date = get_current_date()
    files, stats = find_files(path, filter_expr)
    for file, size in files.items():
        print(date + "\t" + "<FILE>\t" + file + "\t\t" + str(size) + " bytes")
    print()
    print(str(stats['total_files']) + "File(s)" + '\t' + str(stats['total_file_size']) + " bytes")
    print(str(stats['free_disk_space']) + " bytes free")


def display_details(values):
    path = values['path']
    filter_expr = values['filter']
    window['output'].Update('')
    if values['directories']:
        display_files_directories(path, filter_expr)
    else:
        display_files(path, filter_expr)


if __name__ == '__main__':
    window = sg.Window('File Explorer', layout)

    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'find':
            display_details(values)
        elif event == 'clear':
            window['output'].Update('')
    window.Close()
