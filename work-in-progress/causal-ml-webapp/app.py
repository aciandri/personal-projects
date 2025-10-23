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

    readme_tab, setup_tab, results_tab = st.tabs(["Read me", "SetUp Analysis", "Results"])
    readme_tab.write(dict_texts["readme"], unsafe_allow_html=True)

    with setup_tab:
        data_manager_instance = components.DataManager()
        flag_get_data = data_manager_instance.file_upload()

    with results_tab:
        if not flag_get_data:
            st.write("No file loaded yet.")

main()