import streamlit as st
import functions

todos = functions.get_todos()

st.title("My todo app")
st.subheader("This is my Todo app")
st.write("This app is to increase your Productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")

print("Hello")