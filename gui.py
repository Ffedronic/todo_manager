import functions
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Type in a todo")
input_box = FreeSimpleGUI.InputText(tooltip="Enter a todo", key="todo")
add_button = FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window("hello GUI",
                              layout=[[label],[input_box, add_button]],
                              font=("Helvetica", 12)
                              )
while True :
    event, values = window.read()
    match event :
        case "Add" :
            todos = functions.get_todos()
            new_todo = values["todo"].title() + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)

        case FreeSimpleGUI.WIN_CLOSED :
            break

window.close()