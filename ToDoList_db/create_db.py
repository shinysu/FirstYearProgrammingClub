from dbutils import execute_query


def create_task_table():
    """
    Builds the sql query to create a new table.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY, 
    taskname TEXT,
    complete BOOLEAN
    );"""
    execute_query(create_table_sql)


def drop_table():
    """
    Builds the sql query to drop a table.
    :return:
    """
    create_table_sql = "DROP TABLE tasks;"
    execute_query(create_table_sql)


if __name__ == "__main__":
    create_task_table()
    #drop_table()