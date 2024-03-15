import streamlit as st
import langchain_helper as helper


st.title("Restuarant Name Generator")
cuisine = st.sidebar.selectbox("Select a cuisine", ("Kenyan", "Italian", "Chinese", "Indian"))

if cuisine:
    response = helper.generate_restuarant_name_and_items(cuisine)
    st.header(response['restuarant_name'].strip().replace('"', ""))
    menu_items = response['menu_items'].strip().split(",")

    st.write("Menu Items")
    for item in menu_items:
        st.write(item.strip())

