import sqlite3
from constants import DB_NAME

def execute_query(sql_query):
    """
    function to execute sql commands
    :return: returns values if select command used
    """
    with sqlite3.connect(DB_NAME) as con:
        cur = con.cursor()
        result = cur.execute(sql_query)
        con.commit()
    return result


def insert_into_tasks(task):
    """
    adds the new task into the database
    :param task: the new task to be added to the table
    """
    sql_query = """INSERT INTO tasks(taskname, complete) VALUES ( '%s', %s )""" % (task, 0)
    execute_query(sql_query)


def mark_task_as_complete(task):
    """
    updates the status of the task as complete
    :param task: ToDo item
    """
    sql_query = """UPDATE tasks SET complete=1 WHERE taskname='%s' and complete=0""" % (task)
    execute_query(sql_query)


def update_task(oldtask, newtask):
    """
    updates the old task with a new task
    :param oldtask: the task that is to be updated
    :param newtask: the new value for the task
    """
    sql_query = """UPDATE tasks SET taskname='%s' WHERE taskname='%s' and complete=0""" % (newtask, oldtask)
    execute_query(sql_query)


def select_all_from_tasks():
    """
    Get all incomplete tasks from the databse
    :return: tasks marked as incomplete in the database
    """
    sql_query = """SELECT taskname FROM tasks where complete = 0"""
    return [result[0] for result in execute_query(sql_query).fetchall()]


if __name__ == "__main__":
    '''insert_into_tasks("task3")
    insert_into_tasks("task4")
    print(select_all_from_tasks())
    mark_task_as_complete("task2")'''
    print(select_all_from_tasks())
    update_task("task3", "task5")
    print(select_all_from_tasks())
