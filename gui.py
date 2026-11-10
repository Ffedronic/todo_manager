import functions
import FreeSimpleGUI
import time
import os

if not os.path.exists('todos_item.txt'):
    with open('todos_item.txt', 'w') as f:
        pass

FreeSimpleGUI.theme("Dark")
label_time = FreeSimpleGUI.Text("",key="time")
label = FreeSimpleGUI.Text("Type in a todo")
input_box = FreeSimpleGUI.InputText(tooltip="Enter a todo", key="todo")
add_button = FreeSimpleGUI.Button("Add")

list_box = FreeSimpleGUI.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = FreeSimpleGUI.Button("Edit")

complete_button = FreeSimpleGUI.Button("Complete")
exit_button = FreeSimpleGUI.Button("Exit")

layout = [[label_time],[label],[input_box, add_button],[list_box, edit_button, complete_button], [exit_button]]
window = FreeSimpleGUI.Window("hello GUI",
                              layout=layout,
                              font=("Helvetica", 12)
                              )
while True :
    event, values = window.read(timeout=200)
    match event :
        case "Add" :
            todos = functions.get_todos()

            new_todo = values["todo"].title() + '\n'
            todos.append(new_todo)

            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit" :
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"].title() + "\n"

                todos = functions.get_todos()

                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                FreeSimpleGUI.popup("please select an item first.", font=("Helvetica", 12))

        case "Complete" :
            try:
                todo_to_complete = values["todos"][0]

                todos = functions.get_todos()
                todos.remove(todo_to_complete)

                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                FreeSimpleGUI.popup("please select an item first.", font=("Helvetica", 12))

        case "Exit" :
            break

        case "todos":
            try :
                window["todo"].update(value=values["todos"][0].replace("\n", ""))

            #if the listBox is empty
            except IndexError:
                pass

        case FreeSimpleGUI.WIN_CLOSED :
            break

    window["time"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

window.close()