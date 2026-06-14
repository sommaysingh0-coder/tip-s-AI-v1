import streamlit as st
import random
import pyjokes
import json


st.set_page_config(page_title="The Tips AI")

st.title("🤖 The Tips AI")
st.write("Created by Sommay Singh")

option = st.selectbox(
    "Choose a feature",
    [
        "Calculator",
        "Guessing Game",
        "Joke",
        "ABCD",
        "Counter",
        "About Creator",
        "storage memory"
    ]
)

# Calculator
if option == "Calculator":
    num1 = st.number_input("First Number")
    op = st.selectbox("Operator", ["+", "-", "*", "/", "%"])
    num2 = st.number_input("Second Number")

    if st.button("Calculate"):

        if op == "+":
            answer = num1 + num2
        elif op == "-":
            answer = num1 - num2
        elif op == "*":
            answer = num1 * num2
        elif op == "/":
            answer = num1 / num2
        elif op == "%":
            answer = num1 % num2

        st.success(f"Answer = {answer}")

# Joke

elif option == "Joke":
    if st.button("Tell Joke"):
        st.write(pyjokes.get_joke())

# ABCD
elif option == "ABCD":
    st.write("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
    st.write("a b c d e f g h i j k l m n o p q r s t u v w x y z")

# Counter
elif option == "Counter":
    limit = st.number_input("Count up to", min_value=1, step=1)

    if st.button("Start Counting"):
        for i in range(1, int(limit) + 1):
            st.write(i)

# Guessing Game
elif option == "Guessing Game":

    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 100)

    guess = st.number_input(
        "Guess a number",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("Check Guess"):

        if guess < st.session_state.secret:
            st.warning("Too Low!")

        elif guess > st.session_state.secret:
            st.warning("Too High!")

        else:
            st.success("Correct!")
            st.session_state.secret = random.randint(1, 100)

# About Creator
elif option == "About Creator":
    st.write("=================About Creator=================")
    st.write("NAME: Sommay Singh")
    st.write("AGE: 13")
    st.write("HOBBIES: Coding, Gaming,love to chess ,and a anime fan")
    st.write("FAVORITE COLOR: Black")   
    st.write("FAVORITE game: Minecraft")
    st.write("FAVORITE anime: Naruto")
# Storage Memory
elif option == "storage memory":
 st.text_input("enter a word for I M  save it in memory")
 st.text_input("enter the meaning of the word for I M  save it in memory")
 try:
     with open("memory.json", "r") as f:
         knowledge = json.load(f)
 except:
     knowledge = {}

 key = st.text_input("Word")

 value = st.text_input("Meaning")

 if st.button("Save"):
     knowledge[key] = value

     with open("memory.json", "w") as f:
        json.dump(knowledge, f)

     st.success("Saved!")