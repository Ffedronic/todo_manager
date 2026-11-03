import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type in a todo")
input_box = FreeSimpleGUI.InputText(tooltip="Enter a todo")
add_button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window("hello GUI", layout=[[label],[input_box, add_button]])
window.read()
window.close()