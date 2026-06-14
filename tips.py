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
# Storage Memory
elif option == "storage memory":
    try:
        with open("memory.json", "r") as f:
            knowledge = json.load(f)
    except:
        knowledge = {}

    st.subheader("🧠 Storage Memory")

    key = st.text_input("Word")
    value = st.text_input("Meaning")

    if st.button("Save"):

        if key and value:

            knowledge[key] = value

            with open("memory.json", "w") as f:
                json.dump(knowledge, f)

            st.success("Saved!")

        else:
            st.error("Please enter both Word and Meaning")

    st.divider()

    search = st.text_input("Search Word")

    if st.button("Find"):

        if search in knowledge:
            st.success(
                f"{search} = {knowledge[search]}"
            )

        else:
            st.error("Word not found")

    st.divider()

    delete_word = st.text_input(
        "Delete Word"
    )

    if st.button("Delete"):

        if delete_word in knowledge:

            del knowledge[delete_word]

            with open("memory.json", "w") as f:
                json.dump(knowledge, f)

            st.success("Deleted!")

        else:
            st.error("Word not found")

    st.divider()

    if st.button("Show All Saved Words"):

        if knowledge:

            for k, v in knowledge.items():
                st.write(
                    f"🔹 {k} = {v}"
                )

        else:
            st.info("Memory is empty")