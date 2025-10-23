import streamlit as st
import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("arashnic/uplift-modeling")

print("Path to dataset files:", path)

class DataManager():
    def __init__(self):
        self.df = pd.DataFrame()

    def file_upload(self) -> str:
        """ 
        Caricamento del file.

        Returns:
            self.uploaded_file (str): Nome del file caricato dall'utente.
        """

        cols = st.columns([1,2,4,1])
        cols[1].write("")

        # Select uploade mode
        sel_mode = cols[1].radio(
            "lol",
            options= self.dict_writings["opz_selectmode"],
            index=None,
            label_visibility="collapsed",
        )
        self._load_data(sel_mode = sel_mode, st_columns = cols)

        return False # TODO: levarlo e mettere questo return nelle fasi successive, magari un bottone di run finale


    @st.cache_data(ttl=600, show_spinner=False)
    def _load_data(self, sel_mode, st_columns):
        # If Excel file --> Choose your file
        if sel_mode in ["Excel file", "File Excel"]:
            self.uploaded_file = st_columns[2].file_uploader(
                label="lol", type=["xlsx"], label_visibility="collapsed"
            )
        # Else --> Work In Progress
        else:
            self.uploaded_file =None
            if sel_mode in ["Connect to DB (WIP)","Connetti DB (WIP)"]:
                with st_columns[2].container(border=True):
                    st.button(label=self.dict_writings["lab_bottone_WIP"], icon=":material/database_upload:", disabled=True)
