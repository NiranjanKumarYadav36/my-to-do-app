import streamlit as st
import functions


# Load existing todos from file
todos = functions.get_todos()


# Function to add a new todo
def todo_to_added():
    new_todo = st.session_state['new'] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


# Streamlit app title and description
st.title("TODO App")
st.write("Welcome to the TODO App! This simple app is designed to help you organize your tasks and boost your productivity.")

# Input field for adding a new todo
st.text_input(label="", placeholder="Enter your todo...", on_change=todo_to_added, key='new')


# Display existing todos with checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # Remove completed todo and update the file
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()





