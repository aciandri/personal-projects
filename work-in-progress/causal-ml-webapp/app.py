# pyenv activate first_env3.9.9
# streamlit run app.py --server.port 8501
# go to: localhost:8501

# ----- Libraries -----
import streamlit as st

import utils

# ----- Logging -----
logger = utils.get_logger(__name__)

# ----- Page configuration -----
st.set_page_config(
    page_title="WebApp",
    page_icon=":panda_face:", # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    layout="wide"
)
st.markdown(f"<style>{open('settings/style.css').read()}</style>", unsafe_allow_html=True) 

def main():
    dict_texts = utils.AppUI().texts

    tab1, tab2 = st.tabs(["Read me", "App"])
    tab1.markdown(dict_texts, unsafe_allow_html=True)

main()