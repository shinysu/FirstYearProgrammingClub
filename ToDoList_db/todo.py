"""
todo.py: Creates a desktop app that can add, delete and edit items to a ToDoList.
         Uses PySimpleGUI as frontend and SQLite database
"""
import PySimpleGUI as sg
from dbutils import insert_into_tasks, select_all_from_tasks, mark_task_as_complete, update_task

tasks = select_all_from_tasks()
layout = [
    [sg.Text('ToDo List',font=("Arial", 14))],
    [sg.InputText('', size=(40, 1), font=("Arial", 14), key='todo_item', enable_events=True),
     sg.Button('Add', bind_return_key=True, font=("Arial", 14), key='add_save', disabled=True)],
    [sg.Listbox(values=tasks, size=(40, 10), font=("Arial", 14), key='items', enable_events=True),
     sg.Button('Edit Task', key='edit', font=("Arial", 14), disabled=True),
     sg.Button('Delete Task', font=("Arial", 14), key='delete', disabled=True),
     ]
]


def enable_buttons():
    """
    Enable the action buttons only when there is an user input.
    'Add' button will be enabled when the user types a non empty task name. 'Edit' and 'Delete' buttons will be
    enabled when the user selects a task to be edited or deleted.
    """
    if values["items"]:
        window.FindElement('delete').Update(disabled=False)
        window.FindElement('edit').Update(disabled=False)
    if values["todo_item"].strip() != '':
        window.FindElement('add_save').Update(disabled=False)


def add_task():
    """
    If the label of add_save button is 'Add', insert the new task to the database. Otherwise, update the selected task with
    the new value.
    """
    if window.FindElement('add_save').GetText() == 'Add':
        insert_into_tasks(values['todo_item'].strip())
    else:
        update_task(values["items"][0], values['todo_item'])
        window.FindElement('add_save').Update("Add")
    update_UI()


def delete_task():
    """
    Remove the selected task and mark them as complete in database
    """
    mark_task_as_complete(values["items"][0])
    update_UI()


def edit_tasks():
    """
    Display the selected task (to be edited) in the text box. Change the label of 'Add' button to 'Save'
    """
    window.FindElement('add_save').Update(disabled=False)
    window.FindElement('todo_item').Update(value=values["items"][0])
    window.FindElement('add_save').Update("Save")


def update_UI():
    """
    uodate the input elements after every event
    """
    tasks = select_all_from_tasks()
    window.FindElement('items').Update(values=tasks)
    window.FindElement('todo_item').Update(value="")


event_actions = {
    "add_save": add_task, "delete": delete_task, "edit": edit_tasks
}

if __name__ == '__main__':
    window = sg.Window('ToDo List', layout)
    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        else:
            enable_buttons()
            event_actions[event]()

    window.Close()
