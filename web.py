import streamlit as st

import functions

todos  = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo.title() + "\n")
    functions.write_todos(todos)

st.title("My Todos App")
st.subheader("This is my todos app")
st.write("This is my app is to increase my productivity.")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label="Todo Input", placeholder="Enter a new todo...", on_change=add_todo, key="new_todo")
