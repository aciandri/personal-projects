import streamlit as st
import os

from .common import load_json

BASE_DIR = os.path.join(os.path.dirname(__file__))

class UIManager:
    """Manages the Streamlit web app interface, including layout, language selection, and text loading."""

    def __init__(self):
        """Initialize the AppUI with a default or stored language."""
        self.language = st.session_state.setdefault("language", "ita")
        self.texts = self._load_texts()
        self._initialize_session()
        self._setup_layout()

    #@st.cache_data
    def _load_texts(self):
        """Load interface texts based on the selected language."""
        return load_json(flag_ita=(self.language == "ita"), file_json="texts")

    def _initialize_session(self):
        """Ensure the session state is synchronized with the current language selection."""
        st.set_page_config(
            page_title="WebApp",
            page_icon=":panda_face:", # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
            layout="wide"
        )
        st.markdown(f"<style>{open(f'settings/style.css').read()}</style>", unsafe_allow_html=True) 

        if st.session_state["language"] != self.language:
            st.session_state["language"] = self.language
            self.texts = self.load_texts()

    def _select_language(self, st_column):
        """Render the language selector and update the interface accordingly."""
        selected_lang = st_column.selectbox("Select language", options=["Italiano", "English"], label_visibility="collapsed")
        if selected_lang != self.language:
            self.language = selected_lang
            st.session_state["language"] = selected_lang
            self.texts = self._load_texts()

    def _setup_layout(self):
        """Set up the main page layout with logo and title."""
        col1, col2, col3 = st.columns([1, 7, 1])
        col1.image(f"{BASE_DIR}/images/image.png", width=100)
        col2.title("WebApp")
        self._select_language(st_column=col3)
        
