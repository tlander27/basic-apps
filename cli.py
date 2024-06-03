from modules import functions
import time

now = time.strftime("%m-%d-%Y %H:%M")
print("Current time: " + now)
while True:
    user_action = input("Type add, show, edit, complete, exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'.lower()) or user_action.startswith('new'.lower()):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)
    elif user_action.startswith('show'.lower()):
        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}: {item}"
            print(row)
    elif user_action.startswith('edit'.lower()):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('complete'.lower()):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} has been removed."
            print(message)
        except IndexError:
            print("Invalid Todo number.")
            continue
    elif user_action.startswith('exit'.lower()):
        break
    else:
        print("Command is not valid")

