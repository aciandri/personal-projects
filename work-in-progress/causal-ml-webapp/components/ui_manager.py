import streamlit as st
from components.utils import load_json


class UIManager:
    """Manages the Streamlit web app interface, including layout, language selection, and text loading."""

    def __init__(self):
        """Initialize the AppUI with a default or stored language."""
        self.language = st.session_state.setdefault("language", "Italiano")
        self._select_language()
        self._initialize_session()

    @st.cache_data
    def _load_texts(_self):
        """Load interface texts based on the selected language."""
        return load_json(flag_ita=(_self.language == "Italiano"), file_json="texts")

    def _initialize_session(self):
        """Ensure the session state is synchronized with the current language selection."""
        if st.session_state["language"] != self.language:
            st.session_state["language"] = self.language
            self.texts = self.load_texts()

    def _setup_layout(self):
        """Set up the main page layout with logo and title."""
        col1, col2, col3 = st.columns([1, 7, 1])
        col1.image("images/image.png", width=100)
        col2.title("WebApp")
        return col3

    def _select_language(self):
        col3 = self._setup_layout()
        """Render the language selector and update the interface accordingly."""
        selected_lang = col3.selectbox("Select language", options=["Italiano", "English"], label_visibility="collapsed")
        if selected_lang != self.language:
            self.language = selected_lang
            st.session_state["language"] = selected_lang
            self.texts = self._load_texts()