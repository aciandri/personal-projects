import streamlit as st

def init_session_state():
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    if 'data' not in st.session_state:
        st.session_state.data = None
    if 'model' not in st.session_state:
        st.session_state.model = None
    # etc.