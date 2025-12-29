import streamlit as st
from .common import load_translations

LANGUAGES = {
    'en': 'English',
    'it': 'Italiano',
}

class Languages():
    def __init__(self):
        self.language = st.session_state.language

    def language_selector(self) -> str:
        """
        Display language selector in sidebar
        """    
        selected = st.sidebar.selectbox(
            "🌐 Language",
            options=list(LANGUAGES.keys()),
            format_func=lambda x: LANGUAGES[x],
            index=list(LANGUAGES.keys()).index(st.session_state.language),
            key='language_selector'
        )
        
        if selected != st.session_state.language:
            st.session_state.language = selected
            st.rerun()
        
        return st.session_state.language

    def t(self, key: str) -> str:
        """Get translation with dot notation support (e.g., 'pages.home.title')"""        
        if 'translations' not in st.session_state or st.session_state.get('trans_lang') != self.language:
            st.session_state.translations = load_translations()
            st.session_state.trans_lang = self.language
        
        # Support nested keys like 'pages.home.title'
        keys = key.split('.')
        value = st.session_state.translations
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, key)
            else:
                return key
        
        return value