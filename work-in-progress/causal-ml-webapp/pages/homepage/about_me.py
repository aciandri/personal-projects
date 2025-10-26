import streamlit as st
import utils

# ----- Page -----
st.title(st.session_state.translations["welcome"])

st.markdown(
    open(f"config/translations/{st.session_state.translations['readme_file']}.txt").read(),
    unsafe_allow_html=True
)