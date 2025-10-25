# pyenv activate first_env3.9.9
# streamlit run app.py --server.port 8501
# go to: localhost:8501

# ----- Libraries -----
import streamlit as st

import utils

# ----- Set up -----
utils.init_session_state()

# Page Configuration
st.set_page_config(
    page_title="Test",
    page_icon=":white_check_mark:", # https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    layout="wide"
)

st.markdown(f"<style>{open('assets/styles/style.css').read()}</style>", unsafe_allow_html=True) 

lang_instance = utils.Languages()

# ----- Pages -----
pages = {
    lang_instance.t('pages.home.title'): [
        st.Page("pages/homepage/read_me.py", title=lang_instance.t('pages.home.readme')),
        st.Page("pages/homepage/about_me.py", title=lang_instance.t('pages.home.aboutme')),
    ],
    # lang_instance.t('nav.analysis'): [
    #     st.Page("pages/analysis/select_data.py", title=lang_instance.t('nav.select_data')),
    #     st.Page("pages/analysis/fine_tuning.py", title=lang_instance.t('nav.fine_tuning')),
    #     st.Page("pages/analysis/display_results.py", title=lang_instance.t('nav.results')),
    # ]
}

# ----- Webapp -----
def main():
    pg = st.navigation(pages)
    pg.run()

if __name__ == "__main__":
    main()