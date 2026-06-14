import streamlit as st
import random
import pyjokes
import json
import string

st.markdown("""
<h1 style='text-align:center;color:white;'>
🤖 THE TIPS AI
</h1>
""", unsafe_allow_html=True)

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
        "storage memory",
        "Password Generator",
        "Dice Roller"

    ]
)

# Calculator
if option == "Calculator":

 st.subheader("🧮 Calculator")

 num1 = st.number_input("First Number")

 op = st.selectbox(
    "Choose Operator",
        ["+", "-", "*", "/", "%"]
)

 num2 = st.number_input("Second Number")

 if st.button("Calculate"):

        try:

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

        except:
            st.error("Calculation Error")
# Joke

elif option == "Joke":

    st.subheader("😂 Joke Generator")

    if st.button("Tell Me A Joke"):

        joke = pyjokes.get_joke()

        st.info(joke)

# ABCD
elif option == "ABCD":
    st.write("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
    st.write("a b c d e f g h i j k l m n o p q r s t u v w x y z")

# Counter
elif option == "Counter":

    st.subheader("🔢 Counter")

    limit = st.number_input(
        "Count Up To",
        min_value=1,
        step=1
    )

    if st.button("Start Counting"):

        for i in range(
            1,
            int(limit) + 1
        ):
            st.write(i)

# Guessing Game
elif option == "Guessing Game":

    st.subheader("🎮 Guessing Game")

    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 100)

    guess = st.number_input(
        "Guess Number",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("Check Guess"):

        if guess < st.session_state.secret:
            st.warning("⬇ Too Low")

        elif guess > st.session_state.secret:
            st.warning("⬆ Too High")

        else:
            st.success("🎉 Correct!")

            st.session_state.secret = (
                random.randint(1, 100)
            )
# About Creator
elif option == "About Creator":

    st.subheader("👨‍💻 About Creator")

    st.write("Name : Sommay Singh")
    st.write("Age : 13")

    st.write(
        "Hobbies : Coding, Chess, Gaming, Anime"
    )

    st.write(
        "Favourite Game : Minecraft"
    )

    st.write(
        "Favourite Anime : Naruto"
    )

    st.write(
        "Project : The Tips AI"
    )

    st.write(
        "Version : 1.0"
    )

    st.success(
        "Made with Python + Streamlit"
    )
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
#Password Generator
elif option == "Password Generator":

    st.subheader(
        "🔑 Password Generator"
    )

    if st.button("Generate"):

        chars = (
            string.ascii_letters
            + string.digits
        )

        password = "".join(
            random.choice(chars)
            for _ in range(12)
        )

        st.success(password)
#Dice Roller
elif option == "Dice Roller":

    st.subheader("🎲 Dice Roller")

    if st.button("Roll Dice"):

        st.success(
            random.randint(1, 6)
        )
#Dice Roller
elif option == "Dice Roller":

    st.subheader("🎲 Dice Roller")

    if st.button("Roll Dice"):

        st.success(
            random.randint(1, 6)
        )
#background
import base64

def add_bg():
    with open("xxxxxx.png", "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()
###########################################
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0a192f;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background-color: #112240 !important;
    color: white !important;
    border-radius: 10px;
}

/* Number Input */
.stNumberInput input {
    background-color: #112240 !important;
    color: white !important;
}

/* Text Input */
.stTextInput input {
    background-color: #112240 !important;
    color: white !important;
}

/* Buttons */
.stButton > button {
    background-color: #1e3a8a !important;
    color: white !important;
    border-radius: 10px;
    border: none;
}

.stButton > button:hover {
    background-color: #2563eb !important;
}

/* Titles */
h1, h2, h3, p, label {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)