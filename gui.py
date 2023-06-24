import functions
import PySimpleGUI as gui
import time

gui.theme("LightPurple")

clock = gui.Text("", key='clock')
label = gui.Text("Type in a todo:")
input_box = gui.InputText(tooltip='Enter your Todo', key="todo")

add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

todos = functions.get_todos("todos.txt")
list_todos = gui.Listbox(values=functions.get_todos("todos.txt"), key="todos",
                         enable_events=True, size=[45,10] )
window = gui.Window('My todo app',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_todos, edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica",15))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match(event):
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                gui.Popup("Please select an item first", font=("Helvectia", 10))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")

            except IndexError:
                gui.Popup("Please select an item first", font=("Helvectia", 10))

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case gui.WIN_CLOSED:
            break


window.close()