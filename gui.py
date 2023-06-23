import functions
import PySimpleGUI as gui

label = gui.Text("Type in a todo:")
input_box = gui.InputText(tooltip='Enter your Todo', key = "todo")
add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
todos = functions.get_todos("todos.txt")
list_todos = gui.Listbox(values= functions.get_todos("todos.txt"), key = "todos",
                         enable_events= True, size= [45,20] )
window = gui.Window('My todo app',
                    layout=[[label], [input_box, add_button], [list_todos, edit_button]],
                    font=("Helvetica",15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match(event):
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case gui.WIN_CLOSED:
            break


window.close()