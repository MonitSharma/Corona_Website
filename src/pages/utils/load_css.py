# here to the load_css function, and load the css file

import streamlit as st


def local_css(file_name):
    """
    Function to load the css stylesheet

    : param file_name: str
    : return : None
    """

    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)