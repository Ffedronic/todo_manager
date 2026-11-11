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

for item in todos:
    st.checkbox(item)
st.text_input(label="Todo Input", placeholder="Enter a new todo...", on_change=add_todo, key="new_todo")