# pyenv activate first_env3.9.9
# streamlit run app.py --server.port 8501
# go to: localhost:8501

# ----- Libraries -----
import streamlit as st

import components

# ----- Logging -----
logger = components.get_logger(__name__)


def main():
    ui_manager_instance = components.UIManager()
    dict_texts = ui_manager_instance.texts

    tab1, tab2 = st.tabs(["Read me", "App"])
    tab1.write(dict_texts["readme"], unsafe_allow_html=True)

main()