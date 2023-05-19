import functions
import PySimpleGUI as gui

label = gui.Text("Type in a todo:")
input_box = gui.InputText(tooltip='Enter your Todo')
add_button = gui.Button("Add")

window = gui.Window('My todo app', layout=[[label], [input_box, add_button]])
window.read()
window.close()