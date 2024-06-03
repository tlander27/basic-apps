import streamlit as st
from modules import functions

todos = functions.get_todos()

# callback function used with input
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("To-do Web App")
st.subheader("Written in Python with Streamlit")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()  # required with checkboxes

st.text_input(label="", placeholder="Add new to-do",
              on_change=add_todo, key="new_todo")


# st.session_state