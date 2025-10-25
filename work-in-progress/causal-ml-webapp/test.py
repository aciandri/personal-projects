import streamlit as st

pages = {
    "Your account": [
        st.Page("pages/page1.py", title="Create your account"),
        st.Page("pages/page2.py", title="Manage your account"),  # Changed to page2.py
    ],
}

def main():
    pg = st.navigation(pages)
    pg.run()

if __name__ == "__main__":
    main()