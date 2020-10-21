import PySimpleGUI as sg
from file_ops import file_write, file_read

filename = 'tasks.txt'
tasks = file_read(filename)

layout = [
    [sg.Text('ToDo',font=("Arial", 14))],
    [sg.InputText('', size=(40,1), font=("Arial", 14), key='todo_item'),
     sg.Button(button_text='Add', font=("Arial", 14), key='add_save')],
    [sg.Listbox(values=tasks, size=(40, 10), font=("Arial", 14), key='items'), sg.Button('Delete', font=("Arial", 14)),
     sg.Button('Edit', font=("Arial", 14))],
]


def add_tasks(values):
    tasks.append(values['todo_item'])
    window.FindElement('todo_item').Update(value="")
    window.FindElement('items').Update(values=tasks)
    window.FindElement('add_save').Update("Add")


def delete_tasks(values):
    try:
        tasks.remove(values["items"][0])
    except IndexError:
        sg.popup("\nChoose a task to delete\n", title="Error!!!", background_color="white", text_color="red", font=("Arial", 14))
    window.FindElement('items').Update(values=tasks)


def edit_tasks(values):
    try:
        edit_val = values["items"][0]
        tasks.remove(edit_val)
        window.FindElement('todo_item').Update(value=edit_val)
        window.FindElement('add_save').Update("Save")
    except IndexError:
        sg.popup("\nChoose a task to edit\n", title="Error!!!", background_color="white", text_color="red", font=("Arial", 14))


if __name__ == '__main__':
    window = sg.Window('ToDo App', layout)
    while True:
        event, values = window.Read()

        if event == "add_save":
            add_tasks(values)
        elif event == "Delete":
            delete_tasks(values)
        elif event == "Edit":
            edit_tasks(values)
        elif event == sg.WINDOW_CLOSED:
            break
    file_write(filename, tasks)
    window.Close()
