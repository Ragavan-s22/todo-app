from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("Time: ", now)

while True:
    user_action = input("Choose any command to execute add, show, complete, exit: ")
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action.title() [4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('complete'):
        user_complete = user_action.title() [9:]

        todos = get_todos()

        todos.pop(user_complete)

        write_todos(todos)


    elif user_action.startswith('edit'):
        number = user_action [5:]

        todos = get_todos()

        number = number - 1
        todos[number] = input("Enter the new todo: ")

        write_todos(todos)

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is invalid")

print("Bye")


