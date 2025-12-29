import streamlit as st
from .common import load_translations

def init_session_state():
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
        st.session_state.translations = load_translations()

    if 'data' not in st.session_state:
        st.session_state.data = None
    if 'model' not in st.session_state:
        st.session_state.model = None
    # etc.