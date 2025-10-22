# ----- Libraries -----
import streamlit as st

from log_config import get_logger
from tools import load_json

# ----- Logging -----
logger = get_logger(__name__)


class AppUI():
    def __init__(self,):
        self.flag_ita=st.session_state["flag_ita"] if "flag_ita" in st.session_state else "Italiano"

    def initialize_session(self):
        if st.session_state.flag_ita != self.flag_ita:
            st.session_state.flag_ita = self.flag_ita
            self.dict_writings = load_json(flag_ita=self.flag_ita, file_json="texts")

    def setup_layout(self,):
        col1, col2, col3 = st.columns([1, 7, 1])
        col1.image("Images/Logo.png", width=100)
        col2.title("WebApp")
        return col3

    def select_language(self, col3):
        selected_lang = col3.selectbox("lol", options=["Italiano", "English"], label_visibility="collapsed")
        self.flag_ita = (selected_lang == "Italiano")
        if "flag_ita" not in st.session_state:
            st.session_state["flag_ita"]=self.flag_ita
        self.dict_writings = load_json(flag_ita=self.flag_ita, file_json="texts")
        self.colonna_approva = "Approva Controllo" if self.flag_ita else "Approve Control" # useful to approve the suggested controls.
