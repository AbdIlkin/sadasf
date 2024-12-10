import streamlit as st
import requests
import json

# Add custom footer
custom_footer_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {
                visibility: hidden;
            }
            footer:after {
                content:'goodbye';
                visibility: visible;
                display: block;
                position: relative;
                padding: 5px;
                top: 2px;
            }
            </style>
            """
st.markdown(custom_footer_style, unsafe_allow_html=True)

# Example app code
st.title("Custom Footer Example")
st.write("This app demonstrates how to customize the footer in a Streamlit app.")
