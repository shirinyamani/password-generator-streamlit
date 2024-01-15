import streamlit as st
from src.main import RandomPass, Pincode, MemoPassword


st.image("./img/pass.png", width=400)
st.title("	:jigsaw: Password Generator")


option = st.radio(
    "Select your desired Pass word type:",
    ("Random Password", "Pincode Password", "Memorable PassCode")
)

if option == "Pincode Password":
    length = st.slider("Select Length of your password", 8, 16)
    generator = Pincode(length)

elif option == "Random Password":
    length = st.slider("Select the len of your random Password", 8, 16)
    include_num = st.toggle("Do you want to include number?")
    include_symbol = st.toggle("Do you want to include Symbol?")
    generator = RandomPass(length, include_num, include_symbol)

elif option == "Memorable PassCode":
    num_words = st.slider("Select number of words",8,16)
    seperator = st.text_input("Seperator", value='-')
    capitalize = st.toggle(" **Capitalized?** :yum:")
    generator = MemoPassword(num_words, seperator, capitalize)

password = generator.generate()
st.write(fr"Your Password is: ```{password}``` ")

