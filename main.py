# from functions import get_todos, write_todos
import functions
# from prompts import user_prompt_action, user_prompt_edit_new_todo
import prompts
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input(prompts.user_prompt_action)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo.title() + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input(prompts.user_prompt_edit_new_todo)
            todos[number] = new_todo.title() + '\n'

            functions.write_todos(todos)
        except ValueError:
            print(prompts.user_prompt_edit_ValueError)
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print(prompts.user_prompt_complete_IndexError)
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print(prompts.user_prompt_action_Error)

print("Bye!")
