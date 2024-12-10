import streamlit as st

# CSS to hide Streamlit elements
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# App content
st.title("Test App")
st.write("Check if the footer and menu are hidden.")
