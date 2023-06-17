import streamlit as st
import pandas as pd
import pygwalker as pyg

# Set page configuration
st.set_page_config(
    page_title="PyGWalker Demo",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load Data
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df
df = load_data("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Set title and subtitle
st.title('PyGWalker Demo App')
st.subheader('A demonstration of the PyGWalker Python library')

# Display PyGWalker
def load_config(file_path):
    with open(file_path, 'r') as config_file:
        config_str = config_file.read()
    return config_str
config = load_config('config.json')
pyg.walk(df, env='Streamlit', dark='dark', spec=config)