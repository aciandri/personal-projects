# pyenv activate first_env3.9.9
# streamlit run app.py --server.port 8501
# go to: localhost:8501

# ----- Libraries -----
import streamlit as st

import utils.utils as utils

# ----- Pages -----
pages = {
    "Home": [
        st.Page("homepage/read_me.py", title="Readme"),
        st.Page("homepage/about_me.py", title="About me"), 
    ],
    "Analysis": [
        st.Page("analysis/select_data.py", title="Select your data"),
        st.Page("analysis/fine_tuning.py", title="Fine Tuning (Optional)"),
        st.Page("analysis/display_results.py", title="Your results"), 
    ]
}