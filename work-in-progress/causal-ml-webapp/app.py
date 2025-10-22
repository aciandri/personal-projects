# ----- Libraries -----
import streamlit as st

import utils

# ----- Logging -----
logger = utils.get_logger(__name__)

# ----- Page configuration -----
st.set_page_config(
    page_title="AI Data Quality",
    page_icon=":white_check_mark:", # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    layout="wide"
)

st.markdown(f"<style>{open('settings/style.css').read()}</style>", unsafe_allow_html=True) 

def main():
    st.write('something')

main()