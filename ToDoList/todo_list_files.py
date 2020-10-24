import PySimpleGUI as sg
from file_ops import file_write, file_read

filename = 'tasks.txt'
tasks = file_read(filename)

layout = [
    [sg.Text('Week1',font=("Arial", 14))],
    [sg.InputText('', size=(40,1), font=("Arial", 14), key='todo_item', enable_events=True),
     sg.Button(button_text='Add', bind_return_key=True, font=("Arial", 14), key='add_save', disabled=True)],
    [sg.Listbox(values=tasks, size=(40, 10), font=("Arial", 14), key='items', enable_events=True),
     sg.Button('Delete', font=("Arial", 14), key='delete', disabled=True),
     sg.Button('Edit', key='edit', font=("Arial", 14), disabled=True)],
]

def check_enable_buttons():
    if values["items"]:
        window.FindElement('delete').Update(disabled=False)
        window.FindElement('edit').Update(disabled=False)
    if values["todo_item"].strip() != '':
        window.FindElement('add_save').Update(disabled=False)

def add_tasks(values):
    newtask = values['todo_item'].strip()
    if newtask:
        tasks.append(newtask)
    window.FindElement('todo_item').Update(value="")
    window.FindElement('items').Update(values=tasks)
    window.FindElement('add_save').Update("Add")
    window.FindElement('add_save').Update(disabled=True)


def delete_tasks(values):
    tasks.remove(values["items"][0])
    window.FindElement('items').Update(values=tasks)


def edit_tasks(values):
    edit_val = values["items"][0]
    print(edit_val)
    tasks.remove(edit_val)
    window.FindElement('todo_item').Update(value=edit_val)
    window.FindElement('add_save').Update("Save")


if __name__ == '__main__':
    window = sg.Window('Week1 App', layout)
    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        else:
            check_enable_buttons()
        if event == "add_save":
            add_tasks(values)
        elif event == "delete":
            delete_tasks(values)
        elif event == "edit":
            edit_tasks(values)

    file_write(filename, tasks)
    window.Close()
