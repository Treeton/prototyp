# 3rd party module
import streamlit as st

import webbrowser
import os

# custom modules
from tools import file_input


def show():

    # styling
    css = file_input.get_css('css/report.css')
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

    # buttons
    if st.button('Generate Report'):

        webbrowser.open_new(os.getcwd() + '/tmp/report.pdf')
    st.button('Request a Quote')
