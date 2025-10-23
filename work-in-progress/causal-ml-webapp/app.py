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
    flag_ita = st.session_state["language"] == "Italiano"

    readme_tab, setup_tab, results_tab = st.tabs(["Read me", "Setup Analysis", "Results"])
    readme_tab.write(dict_texts["readme"], unsafe_allow_html=True)

    with setup_tab:
        data_manager_instance = components.DataManager(
            dict_texts=dict_texts,
            flag_ita=flag_ita
        )
        flag_get_data = data_manager_instance.file_upload()

    with results_tab:
        if not flag_get_data:
            st.write("No file loaded yet.")

main()