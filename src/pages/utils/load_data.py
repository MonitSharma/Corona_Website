import pandas as pd
import streamlit as st


@st.cache
def load_data(DATA_URL, nrows=None):
    """
    Function that reads data from the url and returns a pandas dataframe
    :param DATA_URL:
    :param nrows:
    :return:
    """

    df = pd.read_csv(DATA_URL, nrows=nrows)

    return df
