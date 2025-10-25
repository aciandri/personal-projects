import streamlit as st
import json
import streamlit as st
from pathlib import Path

LANGUAGES = {
    'en': 'English',
    'it': 'Italiano',
    # 'es': 'Español',
    # 'fr': 'Français',
}

class Languages():
    def __init__(self):
        self.language = self._language_selector()

    def _language_selector(self) -> str:
        """Display language selector in sidebar"""    
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

    def _load_translations(self) -> dict:
        """Load translations from JSON file"""
        file_path = Path(f"config/translations/{self.language}.json")
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            st.write(f"Unable to find translation file for language {self.language}")
        return {}

    def t(self, key: str) -> str:
        """Get translation with dot notation support (e.g., 'pages.home.title')"""        
        if 'translations' not in st.session_state or st.session_state.get('trans_lang') != self.language:
            st.session_state.translations = self._load_translations()
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