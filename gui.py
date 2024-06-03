from modules import functions
import FreeSimpleGUI as sg
import os

# create dependent file if it doesn't exist
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkGrey6")

# gui layout
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add", tooltip=" Add To-do ")
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit", tooltip=" Edit To-do ")
complete_button = sg.Button("Complete", tooltip=" Complete To-do ")
exit_button = sg.Button("Exit", tooltip=" Exit App ")

layout = [
    [label],
    [input_box, add_button],
    [list_box, [edit_button, complete_button]],
    [exit_button]
]

# create window object with layout elements
window = sg.Window("My To-Do App",
                   layout,
                   font=("Helvetica", 12))

# button event functionality
while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            input_box.Update("")
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                input_box.Update("")
            except IndexError:
                sg.popup("Please select an item first.")
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.")
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        # required when closing without exit button
        case sg.WIN_CLOSED:
            break

window.close()