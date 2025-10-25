import streamlit as st
import utils

# ----- Init -----
logger = utils.get_logger(__name__)
translator = utils.Languages().t

# ----- Page -----
st.title(translator('home.welcome'))

st.write('prova per pagina 2')