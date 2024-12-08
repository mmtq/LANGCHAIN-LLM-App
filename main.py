import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

animal_type = st.sidebar.text_input("Enter the type of pet:")

if animal_type :
    color_label = f"Enter the color of the {animal_type}"
    color = st.sidebar.selectbox(color_label, ["White" , "Black", "Brown", "Gray", "Blue", "Green", "Other"])

if st.button("Generate Name"):
    st.write(f"Generating pet names for {animal_type} with color {color}...")
    name = lch.generate_pet_name(animal_type, color)
    if "names" in name:
        for i, pet_name in enumerate(name["names"], 1):
                st.write(f"{i}. {pet_name}")
    else:
        st.error("Could not generate names.")
        