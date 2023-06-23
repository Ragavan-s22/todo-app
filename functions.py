def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of todos """
    with open("todos.txt", 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg , filepath="todos.txt"):
    """ '"""
    with open("todos.txt", 'w') as file_local:
        file_local.writelines(todos_arg)
